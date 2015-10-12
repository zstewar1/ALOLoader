import sys, os

bl_info = {
    'name': 'ALO Import',
    'author': 'Zachary Stewart',
    'location': 'File > Import-Export',
    'category': 'Import-Export',
}

if 'bpy' in locals():
    import importlib
    importlib.reload(chunkedparse)
    importlib.reload(aloformat)
    print('Reloaded ALO Import')
else:
    from . import chunkedparse, aloformat
    print('Imported ALO Import')

import bpy, os, bmesh
from bpy_extras.io_utils import ImportHelper
from mathutils import Matrix, Vector

class ALOImportError(Exception):
    pass

class IMPORT_OT_alo(bpy.types.Operator, ImportHelper):
    bl_idname = 'io_import_scene.alo'
    bl_description = 'Import from ALO file format (.alo)'
    bl_label = 'Import ALO'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    filename_ext = '.alo'
    filter_glob = bpy.props.StringProperty(default='*.alo', options={'HIDDEN'})

    scale = bpy.props.FloatProperty(
        name='Scale',
        description='Scale mesh',
        default = 0.1, min=0.001, max=1000)

    filepath = bpy.props.StringProperty(
        name='File Path', description='File path used for importing the ALO file')

    def execute(self, context):
        print('Load', self.properties.filepath)
        name = os.path.splitext(os.path.basename(self.properties.filepath))[0]
        print(name)
        realpath = os.path.realpath(os.path.expanduser(self.properties.filepath))

        with open(realpath, 'rb') as file:
            print('Importing', realpath)
            buf = bytearray(file.read())

        model = chunkedparse.parse_chunked(aloformat.aloformat, buf)

        ske = model['skeleton']
        if len(ske) != 1:
            raise ALOImportError('Skeleton should have exactly 1 item')

        ske = ske[0]
        bones = ske['bone_container']

        if not bones:
            raise ALOImportError('No bones')

        bpy.ops.object.armature_add()
        armature_object = bpy.context.scene.objects.active
        armature_object.name = name + '_skeleton'
        armature = armature_object.data

        bpy.ops.object.mode_set(mode='EDIT')

        ebs = list(armature.edit_bones)
        for eb in ebs:
            armature.edit_bones.remove(eb)

        for bone in bones:
            eb = armature.edit_bones.new(bone['name_container'][0]['name'])
            bd = bone['bone'][0]
            if bd['parent'] >= 0:
                eb.parent = armature.edit_bones[bd['parent']]

            mat = Matrix(bd['matrix'] + [(0,0,0,1)])
            if eb.parent:
                mat = eb.parent.matrix * mat

            eb.matrix = mat

            eb.tail = eb.head + Vector((0, 1, 0))

            eb.tail *= self.scale
            eb.head *= self.scale

        bpy.ops.object.mode_set(mode='OBJECT')

        for me in model['mesh']:
            name = me['mesh_name'][0]['name']

            subdat = me['sub_mesh_data'][0]
            vertbuf = subdat['vertex_buffer'][0]['buffer']

            verts = []
            norms = []
            for v in vertbuf:
                pos = Vector(v['position']) * self.scale
                norm = Vector(v['normal'])
                lm = armature.bones[name].matrix_local
                verts.append(lm * pos)
                norms.append(lm.to_3x3() * norm)

            texcoords = [[v['tex_coords'][i] for v in vertbuf] for i in range(4)]

            group_faces = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
            faces = group_faces(subdat['index_buffer'][0]['indices'], 3)

            mesh = bpy.data.meshes.new(name)

            mesh.from_pydata(verts, [], faces)

            for i, vert in enumerate(mesh.vertices):
                vert.normal = norms[i]

            scn = bpy.context.scene
            ob = bpy.data.objects.new(name, mesh)
            ob.location = armature_object.location
            scn.objects.link(ob)
            scn.objects.active = ob

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func_import(self, context):
    self.layout.operator(IMPORT_OT_alo.bl_idname, text='ALO (.alo)')

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)

if __name__ == '__main__':
    register()

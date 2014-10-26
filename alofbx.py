try:
    from Python33_x64 import fbx
except ImportError:
    from Python33_x86 import fbx

import numpy
import sys

def dump(alo, fp):
    raise NotImplementedError('FBX output is not implemented')

    sdk_manager = fbx.FbxManager.Create()
    scene = fbx.FbxScene.Create(sdk_manager, '')

    objects = fill_scene(alo, scene)

    io_settings = fbx.FbxIOSettings.Create(sdk_manager, fbx.IOSROOT)
    sdk_manager.SetIOSettings(io_settings)

    exporter = fbx.FbxExporter.Create(sdk_manager, '')
    fp.close()
    exp_status = exporter.Initialize(fp.name, -1, sdk_manager.GetIOSettings())

    if exp_status:
        exporter.Export(scene)
    else:
        print('Error setting up exporter', file=sys.stderr)

    exporter.Destroy()
    io_settings.Destroy()

    for obj in reversed(objects):
        obj.Destroy()

    scene.Destroy()
    sdk_manager.Destroy()

def fill_scene(alo, scene):
    objects = []

    bones = []



    return objects    

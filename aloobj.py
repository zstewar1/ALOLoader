import itertools
import numpy


def dump(alo, fp):
    bones = alo['skeleton'][0]['bone_container']
    for bone in bones:
        b = bone['bone'][0]
        b['matrix'].append((0, 0, 0, 1))
        b['matrix'] = numpy.matrix(b['matrix'])
        b['pmatrix'] = b['matrix']
        if b['parent'] >= 0:
            b['pmatrix'] = bones[b['parent']]['bone'][0]['pmatrix'] * b['pmatrix']

    verts = {}
    vertr = {}
    tex = {}
    texr = {}
    norm = {}
    normr = {}

    for meshindex, mesh in enumerate(alo['mesh']):
        print('g', mesh['mesh_name'][0]['name'], file=fp)

        conn = next(c for c in alo['connections'][0]['object_connection']
                    if c['object'] == meshindex)
        if conn:
            matrix = bones[conn['bone']]['bone'][0]['pmatrix']
        else:
            matrix = numpy.matrix(numpy.identity(4))


        for submesh in mesh['sub_mesh_data']:

            verto = []
            texo = []
            normo = []

            for vert in submesh['vertex_buffer'][0]['buffer']:
                mpos = matrix * numpy.matrix(vert['position'] + (1,)).T
                pos = tuple(itertools.islice(mpos.flat, 3))
                verti = vertr.setdefault(pos, len(verts))
                if verti == len(verts):
                    print('v', *pos, file=fp)
                verts.setdefault(verti, pos)
                verto.append(verti + 1)

                texc = vert['tex_coords'][0]
                texi = texr.setdefault(texc, len(tex))
                if texi == len(tex):
                    print('vt', *texc, file=fp)
                tex.setdefault(texi, texc)
                texo.append(texi + 1)

                mnormv = numpy.matrix(vert['normal']) * matrix[:3,:3].I
                normv = tuple(mnormv.flat)
                normi = normr.setdefault(normv, len(norm))
                if normi == len(norm):
                    print('vn', *normv, file=fp)
                norm.setdefault(normi, normv)
                normo.append(normi + 1)

            ib = submesh['index_buffer'][0]['indices']
            for i in range(0, len(ib), 3):
                print('f ', sep='', end='', file=fp)
                print(verto[ib[i]], texo[ib[i]], normo[ib[i]], sep='/', end='', file=fp)
                print(' ', sep='', end='', file=fp)
                print(
                    verto[ib[i+1]], texo[ib[i+1]], normo[ib[i+1]], sep='/', end='',
                    file=fp)
                print(' ', sep='', end='', file=fp)
                print(
                    verto[ib[i+2]], texo[ib[i+2]], normo[ib[i+2]], sep='/', end='\n',
                    file=fp)


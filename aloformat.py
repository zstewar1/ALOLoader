aloformat = {
    65537: {
        'content': [
            {
                'type': '<I',
                'name': 'num_verts',
            },
            {
                'type': '<I',
                'name': 'num_primitives',
            },
            {
                'type': '120x'
            },
        ],
        'head': 65537,
        'name': 'sub_mesh_information',
    },
    65540: {
        'content': [
            {
                'type': '<H',
                'count': {
                    'property': 'num_primitives',
                    'chunk_name': 'sub_mesh_information',
                    'scale': 3,
                },
                'name': 'indices',
            },
        ],
        'head': 65540,
        'name': 'index_buffer',
    },
    65542: {
        'content': [
            {
                'type': '<I',
                'count': 'max',
                'name': 'bone',
            }
        ],
        'head': 65542,
        'name': 'animation_mapping'
    },
    513: {
        'content': [
            {
                'type': '<I',
                'name': 'num_bones',
            },
            {
                'type': '124x',
            },
        ],
        'head': 513,
        'name': 'bone_count',
    },
    65538: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'format',
            },
        ],
        'head': 65538,
        'name': 'vertex_format',
    },
    1536: {
        'head': 1536,
        'name': 'connections',
    },
    65793: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 65793,
        'name': 'shader_filename',
    },
    65543: {
        'content': [
            {
                'type': 'struct',
                'content': [
                    {
                        'type': '<3f',
                        'name': 'position',
                    },
                    {
                        'type': '<3f',
                        'name': 'normal',
                    },
                    {
                        'type': '<2f',
                        'count': 4,
                        'name': 'tex_coords',
                    },
                    {
                        'type': '<3f',
                        'name': 'tangent',
                    },
                    {
                        'type': '<3f',
                        'name': 'binormal',
                    },
                    {
                        'type': '<4f',
                        'name': 'color',
                    },
                    {
                        'type': '<16x',
                    },
                    {
                        'type': '<4I',
                        'name': 'bone_indices',
                    },
                    {
                        'type': '<4f',
                        'name': 'bone_weights',
                    },
                ],
                'count': {
                    'property': 'num_verts',
                    'chunk_name': 'sub_mesh_information',
                },
                'name': 'buffer',
            },
        ],
        'head': 65543,
        'name': 'vertex_buffer',
    },
    517: {
        'content': [
            {
                'type': '<i',
                'name': 'parent',
            },
            {
                'type': '<I',
                'name': 'visible',
            },
            {
                'type': '<4i',
                'name': 'matrix',
                'count': 3,
            },
        ],
        'head': 517,
        'name': 'bone',
    },
    1025: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 1025,
        'name': 'mesh_name',
    },
    65797: {
        'content': [
            {
                'type': 'asciiz',
                'head': 1,
                'name': 'name',
            },
            {
                'type': 'asciiz',
                'head': 2,
                'name': 'value',
            },
        ],
        'head': 65797,
        'name': 'shader_parameter_texture',
    },
    1538: {
        'content': [
            {
                'type': '<I',
                'head': 2,
                'name': 'object',
            },
            {
                'type': '<I',
                'head': 3,
                'name': 'bone',
            },
        ],
        'head': 1538,
        'name': 'object_connection',
    },
    65541: {
        'content': [
            {
                'type': 'struct',
                'content': [
                    {
                        'type': '<3f',
                        'name': 'position',
                    },
                    {
                        'type': '<3f',
                        'name': 'normal',
                    },
                    {
                        'type': '<2f',
                        'count': 4,
                        'name': 'tex_coords',
                    },
                    {
                        'type': '<3f',
                        'name': 'tangent',
                    },
                    {
                        'type': '<3f',
                        'name': 'binormal',
                    },
                    {
                        'type': '<4f',
                        'name': 'color',
                    },
                    {
                        'type': '<4I',
                        'name': 'bone_indices',
                    },
                    {
                        'type': '<4f',
                        'name': 'bone_weights',
                    },
                ],
                'count': {
                    'property': 'num_verts',
                    'chunk_name': 'sub_mesh_information',
                },
                'name': 'buffer',
            },
        ],
        'head': 65541,
        'name': 'vertex_buffer',
    },
    515: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 515,
        'name': 'name_container',
    },
    1024: {
        'head': 1024,
        'name': 'mesh',
    },
    514: {
        'head': 514,
        'name': 'bone_container',
    },
    512: {
        'head': 512,
        'name': 'skeleton',
    },
    65796: {
        'content': [
            {
                'type': 'asciiz',
                'head': 1,
                'name': 'name',
            },
            {
                'type': '<3f',
                'head': 2,
                'name': 'value',
            },
        ],
        'head': 65796,
        'name': 'shader_parameter_float',
    },
    1026: {
        'content': [
            {
                'type': '<I',
                'name': 'num_materials',
            },
            {
                'type': '<3f',
                'count': 2,
                'name': 'boundingBox',
            },
            {
                'type': '4x',
            },
            {
                'type': '<I',
                'name': 'is_hidden',
            },
            {
                'type': '<I',
                'name': 'is_collision_enabled',
            },
            {
                'type': '88x',
            },
        ],
        'head': 1026,
        'name': 'mesh_information',
    },
    65794: {
        'content': [
            {
                'type': 'asciiz',
                'head': 1,
                'name': 'name',
            },
            {
                'type': '<i',
                'head': 2,
                'name': 'value',
            },
        ],
        'head': 65794,
        'name': 'shader_parameter_int',
    },
    65792: {
        'head': 65792,
        'name': 'sub_mesh_material_info',
    },
    65798: {
        'content': [
            {
                'type': 'asciiz',
                'head': 1,
                'name': 'name',
            },
            {
                'type': '<4f',
                'head': 2,
                'name': 'value',
            },
        ],
        'head': 65798,
        'name': 'shader_parameter_float',
    },
    518: {
        'content': [
            {
                'type': '<i',
                'name': 'parent',
            },
            {
                'type': '<I',
                'name': 'visible',
            },
            {
                'type': '<I',
                'name': 'billboard',
            },
            {
                'type': '<4f',
                'name': 'matrix',
                'count': 3,
            },
        ],
        'head': 518,
        'name': 'bone',
    },
    65795: {
        'content': [
            {
                'type': 'asciiz',
                'head': 1,
                'name': 'name',
            },
            {
                'type': '<f',
                'head': 2,
                'name': 'value',
            },
        ],
        'head': 65795,
        'name': 'shader_parameter_float',
    },
    65536: {
        'head': 65536,
        'name': 'sub_mesh_data',
    },
}

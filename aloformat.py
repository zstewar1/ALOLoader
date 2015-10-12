aloformat = {
    0x10001: {
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
        'head': 0x10001,
        'name': 'sub_mesh_information',
    },
    0x10004: {
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
        'head': 0x10004,
        'name': 'index_buffer',
    },
    0x10006: {
        'content': [
            {
                'type': '<I',
                'count': 'max',
                'name': 'bone',
            }
        ],
        'head': 0x10006,
        'name': 'animation_mapping'
    },
    0x201: {
        'content': [
            {
                'type': '<I',
                'name': 'num_bones',
            },
            {
                'type': '124x',
            },
        ],
        'head': 0x201,
        'name': 'bone_count',
    },
    0x10002: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'format',
            },
        ],
        'head': 0x10002,
        'name': 'vertex_format',
    },
    0x600: {
        'head': 0x600,
        'name': 'connections',
    },
    0x10101: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 0x10101,
        'name': 'shader_filename',
    },
    0x10007: {
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
        'head': 0x10007,
        'name': 'vertex_buffer',
    },
    0x205: {
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
        'head': 0x205,
        'name': 'bone',
    },
    0x401: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 0x401,
        'name': 'mesh_name',
    },
    0x10105: {
        'content': [
            {
                'type': 'asciiz',
                'head': 0x1,
                'name': 'name',
            },
            {
                'type': 'asciiz',
                'head': 0x2,
                'name': 'value',
            },
        ],
        'head': 0x10105,
        'name': 'shader_parameter_texture',
    },
    0x602: {
        'content': [
            {
                'type': '<I',
                'head': 0x2,
                'name': 'object',
            },
            {
                'type': '<I',
                'head': 0x3,
                'name': 'bone',
            },
        ],
        'head': 0x602,
        'name': 'object_connection',
    },
    0x10005: {
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
        'head': 0x10005,
        'name': 'vertex_buffer',
    },
    0x203: {
        'content': [
            {
                'type': 'asciiz',
                'name': 'name',
            },
        ],
        'head': 0x203,
        'name': 'name_container',
    },
    0x400: {
        'head': 0x400,
        'name': 'mesh',
    },
    0x202: {
        'head': 0x202,
        'name': 'bone_container',
    },
    0x200: {
        'head': 0x200,
        'name': 'skeleton',
    },
    0x10104: {
        'content': [
            {
                'type': 'asciiz',
                'head': 0x1,
                'name': 'name',
            },
            {
                'type': '<3f',
                'head': 0x2,
                'name': 'value',
            },
        ],
        'head': 0x10104,
        'name': 'shader_parameter_float',
    },
    0x402: {
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
        'head': 0x402,
        'name': 'mesh_information',
    },
    0x10102: {
        'content': [
            {
                'type': 'asciiz',
                'head': 0x1,
                'name': 'name',
            },
            {
                'type': '<i',
                'head': 0x2,
                'name': 'value',
            },
        ],
        'head': 0x10102,
        'name': 'shader_parameter_int',
    },
    0x10100: {
        'head': 0x10100,
        'name': 'sub_mesh_material_info',
    },
    0x10106: {
        'content': [
            {
                'type': 'asciiz',
                'head': 0x1,
                'name': 'name',
            },
            {
                'type': '<4f',
                'head': 0x2,
                'name': 'value',
            },
        ],
        'head': 0x10106,
        'name': 'shader_parameter_float',
    },
    0x206: {
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
        'head': 0x206,
        'name': 'bone',
    },
    0x10103: {
        'content': [
            {
                'type': 'asciiz',
                'head': 0x1,
                'name': 'name',
            },
            {
                'type': '<f',
                'head': 0x2,
                'name': 'value',
            },
        ],
        'head': 0x10103,
        'name': 'shader_parameter_float',
    },
    0x10000: {
        'head': 0x10000,
        'name': 'sub_mesh_data',
    },
}

#!/usr/bin/env python3

import aloobj
import argparse
import collections
import json
import struct
import sys

def load_format(file):
    return {int(k): v for k,v in json.load(file).items()}

def parse_chunked(format, buf):
    chunk_data = collections.defaultdict(list)

    while buf:
        chunk_id, size = unpack('<Ii', buf)

        sub_chunks = size < 0
        size = abs(size)

        chunk_type = format.get(chunk_id)

        if chunk_type:
            if sub_chunks:
                chunk_data[chunk_type['name']].append(parse_chunked(format, buf[:size]))
            else:
                chunk_data[chunk_type['name']].append(parse_chunk(
                    chunk_type, buf[:size], chunk_data))
        del buf[:size]

    return chunk_data

def unpack(format, buf):
    """Both unpack and delete. Convert single-element tuples to their element"""
    result = struct.unpack_from(format, buf)
    if len(result) == 1:
        result = result[0]
    del buf[:struct.calcsize(format)]
    return result

def unpack_asciiz(buf):
    l = buf.find(b'\x00')
    if l < 0:
        # should not happen (famous last words), but if it does, interpret the whole
        # bytearray as a string and delete all of its contents (by setting the end
        # character to past the end
        l = len(buf)

    result = buf[:l].decode(encoding='ascii')
    del buf[:l+1]
    return result

def parse_chunk(format, buf, parent):
    result = {}
    content = format.get('content')
    if not content:
        raise InvalidOperationException(
            'Attempting to get a content chunk from a format that does not contain a '
            'content')

    for c in content:
        name = c.get('name')
        t = c['type']

        if c.get('head'):
            del buf[:2]

        if name is None:
            del buf[:struct.calcsize(t)]
            continue

        ct = c.get('count')
        if isinstance(ct, dict):
            # always take the first element of the given chunk type.
            ct = parent[ct['chunk_name']][0][ct['property']]

        if ct is None:
            if t == 'asciiz':
                result[name] = unpack_asciiz(buf)
            elif t == 'struct':
                result[name] = parse_chunk(c, buf, parent)
            else:
                result[name] = unpack(t, buf)
        elif ct == 'max':
            result[name] = []
            while buf:
                if t == 'asciiz':
                    result[name].append(unpack_asciiz(buf))
                elif t == 'struct':
                    result[name].append(parse_chunk(c, buf, parent))
                else:
                    result[name].append(unpack(t, buf))
        else:
            result[name] = []
            for _ in range(ct):
                if t == 'asciiz':
                    result[name].append(unpack_asciiz(buff))
                elif t == 'struct':
                    result[name].append(parse_chunk(c, buf, parent))
                else:
                    result[name].append(unpack(t, buf))

    return result

def main(args):
    with args.json_file as json_file, args.chunked_file as chunked_file,\
        args.output_file as output_file:

        format = load_format(json_file)
        buf = bytearray(chunked_file.read())

        parse_result = parse_chunked(format, buf)

        if args.output_format == 'dict':
            print(parse_result, file=args.output_file)
        elif args.output_format == 'json':
            json.dump(parse_result, output_file)
            print(file=args.output_file)
        elif args.output_format == 'obj':
            aloobj.dump(parse_result, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Load chunked files based on a json descripton')
    parser.add_argument(
        'json_file', type=argparse.FileType('r'),
        help='The json file which describes the chunked format to be used')
    parser.add_argument(
        'chunked_file', type=argparse.FileType('rb'),
        help='The chunked file to be red using the specified format')
    parser.add_argument(
        '--output-format', '-f', type=str, choices=('dict', 'json', 'obj'),
        default='dict', help='The output format of the resulting data')
    parser.add_argument(
        '--output-file', '-o', type=argparse.FileType('w'), default=sys.stdout,
        help='where to store the output of the operation (default: stdout)')


    main(parser.parse_args())

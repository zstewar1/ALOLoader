import collections
import struct

from aloformat import aloformat

def parse_chunked(buf):
    chunk_data = collections.defaultdict(list)

    while buf:
        chunk_id, size = unpack('<Ii', buf)

        sub_chunks = size < 0
        # Clear the sign bit (used to indicate if a chunk contains sub-chunks)
        size &= 0x7fffffff

        chunk_type = aloformat.get(chunk_id)

        if chunk_type:
            if sub_chunks:
                chunk_data[chunk_type['name']].append(parse_chunked(buf[:size]))
            else:
                chunk_data[chunk_type['name']].append(parse_chunk(
                    chunk_type, buf[:size], chunk_data))
        del buf[:size]

    return chunk_data

def unpack(fmt, buf):
    """Both unpack and delete. Convert single-element tuples to their element"""
    result = struct.unpack_from(fmt, buf)
    if len(result) == 1:
        result = result[0]
    del buf[:struct.calcsize(fmt)]
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

def parse_chunk(fmt, buf, parent):
    result = {}
    content = fmt['content']

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
            ct = parent[ct['chunk_name']][0][ct['property']] * ct.get('scale', 1)

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

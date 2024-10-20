#!/usr/bin/env python

ascii_demo = b'\x41'
utf8_demo = b'\xf0\x9f\x98\x8d'

def format_binary(byte):
    return bin(byte)[2:].rjust(8, "0")

def format_hex(bytes):
    output = ''
    bytes = bytes[::-1]
    while len(bytes):
        output += bytes[:2][::-1].rjust(2, '0')[::-1] + " "
        bytes = bytes[2:]
    return output[::-1].strip()

def output(stream):
    print(f'Decimal:\t{" ".join([str(byte) for byte in stream])}')
    print(f'Hex:\t\t{" ".join([hex(byte)[2:].upper() for byte in stream])}')
    print(f'Binary:\t\t{" ".join([format_binary(byte) for byte in stream])}')
    print()
    print('Type:\t\t', end='')
    if stream[0] & 0x80:
        print('UTF-8 (high bit of all bytes is true)')
        print()
        if len(stream) == 4:
            print('\t\tThere are four bytes total because the first four bits are set:')
            print('\t\t11110___ ________ ________ ________')
            print()
            print('\t\t4 UTF-8 bytes contain 21 bits of info:')
            print('\t\t11110___ 10______ 10______ 10______')
            print()
            print('\t\tThat info is:')
            print(f'\t\t_____{format_binary(stream[0])[5:]}', end='')
            print(f' __{format_binary(stream[1])[2:]}', end='')
            print(f' __{format_binary(stream[2])[2:]}', end='')
            print(f' __{format_binary(stream[3])[2:]}')
            print()
            print('\t\tThose bits concatenated are:')
            info_bin = format_binary(stream[0])[5:] + "".join([format_binary(byte)[2:] for byte in stream[1:]])
            print(f'\t\t{info_bin}')
            print()
            print('\t\tWhich in hex is:')
            info_hex = hex(int(info_bin, 2)).upper()
            print(f'\t\t{format_hex(info_hex[2:])}')
            print()
            print(f'\t\tWhich means the UTF-8 code point is:')
            print(f'\t\tU+{info_hex[2:].upper()}')
    else:
        print('ASCII (high bit of all bytes is false)')
    print()
    print(f'Render:\t\t{stream.decode("utf-8")}')

print()
for i in [ascii_demo, utf8_demo]:
    print('=' * 60)
    print()
    output(i)
    print()
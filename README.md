# Learn how UTF-8 encoding works

A small coding example inspired by [_UTF-8: Bits, Bytes, and Benefits_](https://research.swtch.com/utf8). 

```

============================================================

Decimal:    65
Hex:        41
Binary:     01000001

Type:       ASCII (high bit of all bytes is false)

Render:     A

============================================================

Decimal:    240 159 152 141
Hex:        F0 9F 98 8D
Binary:     11110000 10011111 10011000 10001101

Type:       UTF-8 (high bit of all bytes is true)

            There are four bytes total because the first four bits are set:
            11110___ ________ ________ ________

            4 UTF-8 bytes contain 21 bits of info:
            11110___ 10______ 10______ 10______

            That info is:
            _____000 __011111 __011000 __001101

            Those bits concatenated are:
            000011111011000001101

            Which in hex is:
            01 F6 0D

            Which means the UTF-8 code point is:
            U+1F60D

Render:     😍

```


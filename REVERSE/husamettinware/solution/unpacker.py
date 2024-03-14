import lief

def ror32(num, cnt):
    return (num >> cnt)|(num << 32 - cnt) & 0xFFFFFFFF


# parse elf file
elf_file = lief.parse('solution/husamettinware')

# find text section
text_section = elf_file.get_section('.text')
if text_section is None:
    print('Unable to find text section.')
    exit(1)

key = 0x430a7a2f
# unpack

with open('solution/text_section.bin', 'wb') as fd:
    for idx, byte in enumerate(text_section.content):
        #print('0x{0:0{1}X}'.format(key, 8))
        key_byte = key & 0xff
        val = key_byte ^ byte
        key = ror32(key, 4)
        fd.write(val.to_bytes(1, 'little'))

elf_file.header.entrypoint = text_section.offset
elf_file.write('solution/husamettinware.unpacked')

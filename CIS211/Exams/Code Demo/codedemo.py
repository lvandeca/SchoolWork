def pack_instruction(opcode: int, reg1_add: int, reg2_add: int) -> int:
    packed = opcode
    packed = (packed << 5) | reg1_add
    packed = (packed << 5) | reg2_add
    return packed

def unpack_instruction(packed: int) -> list:
    reg2_add = packed & 0b11111
    reg1_add = (packed >> 5) & 0b11111
    opcode = (packed >> 10) & 0b111
    return [opcode, reg1_add, reg2_add]

def main():
    x = pack_instruction(3, 26, 13)
    print(x)
    print(unpack_instruction(x))

if __name__ == "__main__":
    main()
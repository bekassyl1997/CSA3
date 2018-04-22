import numpy as np
import math

a = np.nan
b = np.nan
content = np.full((5000,), np.nan)
pc = 0
bytes = {0x00: 1, 0x01: 1, 0x02: 1, 0x03: 2, 0x04: 2, 0x05: 3,
         0x06: 3, 0x07: 3, 0x08: 3, 0x09: 1, 0x0A: 1, 0x0B: 1,
         0x0C: 1, 0x0D: 1, 0x0E: 1, 0x0F: 1, 0x10: 1, 0x11: 1,
         0x12: 1, 0x13: 1, 0x14: 1, 0x15: 1, 0x16: 1, 0x17: 3,
         0x18: 3, 0x19: 3, 0x20: 1, 0x21: 1, 0x22: 1, 0x23: 1}
# Read from file function
def readHex():
    fileName = input('Enter the filename: ')
    return open(fileName, 'r').read()
#/////////////////////////////////////////////////////////////

# Task 1
def storeRam(s=''):
    ram = np.array([], dtype=np.uint8)
    for i in range(0, len(s), 2):
        element = s[i:i + 2]
        n = np.uint8(int(element, 16))
        ram = np.append(ram, [n])
    return ram

# Task 2
def alu(a=0, b=0, op=0):
    if op == np.uint8(0x09):
        return np.uint8(a + b)
    if op == np.uint8(0x0A):
        if a >= b:
            return np.uint8(a - b)
        return False
    if op == np.uint8(0x0B):
        return np.uint8(a * b)
    if op == np.uint8(0x0C):
        return np.uint8(a // b)
    if op == np.uint8(0x11):
        return np.uint8(a & b)
    if op == np.uint8(0x12):
        return np.uint8(a | b)
    if op == np.uint8(0x13):
        return np.uint8(a ^ b)
    if op == np.uint8(0x14):
        if a == b:
            return 0
        else:
            return 1
    return False

# Task 3
def updatePC(offset=0):
    global pc
    pc += offset

# Task 4
def controlLogic():
    s = readHex()
    ram = storeRam(s)
    while pc < len(ram):
        offset = bytes[(ram[pc])]
        print(format(ram[pc], '02x'), end=' ')
        if offset == 3:
            print(format(ram[pc + 1], '02x'), end='')
            print(format(ram[pc + 2], '02x'), end=' ')
        elif offset == 2:
            print(format(ram[pc + 1], '02x'), end=' ')
        print()
        updatePC(offset)


# TEST FUNCTIONS
# Final
def finalFunction():
    s = readHex()
    ram = storeRam(s)
    global a
    global b
    global content
    print("A\tB")
    while pc < len(ram):
      #  print(content[pc])
        offset = bytes[(ram[pc])]
     #   print(format(ram[pc], '02x'), end=' ')
        if offset == 3:
            if ram[pc] == 0x05:
                a = content[ram[pc + 1] * 0x100 + ram[pc + 2]]
            elif ram[pc] == 0x06:
                b = content[ram[pc + 1] * 0x100 + ram[pc + 2]]
            elif ram[pc] == 0x07:
                content[ram[pc + 1] * 0x100 + ram[pc + 2]] = a
            elif ram[pc] == 0x08:
                content[ram[pc + 1] * 0x100 + ram[pc + 2]] = b
            elif ram[pc] == 0x17:
                ram[pc + 3] = content[ram[pc + 1] * 0x100 + ram[pc + 2]]
            elif ram[pc] == 0x18:
                if a == 0x00:
                    ram[pc + 3] = content[ram[pc + 1] * 0x100 + ram[pc + 2]]
            elif ram[pc] == 0x19:
                if a != 0x00:
                    ram[pc + 3] = content[ram[pc + 1] * 0x100 + ram[pc + 2]]

            # print(format(ram[pc + 1], '02x'), end='')
            # print(format(ram[pc + 2], '02x'), end=' ')
        elif offset == 2:
            if ram[pc] == 0x03:
                a = ram[pc + 1]
            elif ram[pc] == 0x04:
                b = ram[pc + 1]
        temp = alu(a, b, ram[pc])
        if temp != False:
            a = int(temp)

        if math.isnan(a):
            print("nan", end="\t")
        else:
            print(format(int(a), '02x'), end='\t')

        if math.isnan(b):
            print("nan")
        else:
            print(format(int(b), '02x'))

        updatePC(offset)

    for i in range(5000):
        if math.isnan(content[i]) == False:
            print("Address ", end=" ")
            print(format(i, '04x'), end=": ")
            print(format(int(content[i]), '02x'))


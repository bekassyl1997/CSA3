import numpy as np

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
        if a > b:
            return np.uint8(a)
        else:
            return np.uint8(b)
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
# Task 1
def test1():
    print('TEST: Task 1')
    ram = storeRam(readHex())
    for i in range(len(ram)):
        print(format(ram[i], '02x'))

# Task 2
def test2():
    a, b = 0x3, 0x6
    print('\nTEST: Task 2')
    ram = storeRam(readHex())
    print('Hex:\tAns:')
    for i in range(len(ram)):
        print(format(ram[i], '02x'), end='\t\t')
        ans = alu(a, b, ram[i])
        if ans == False:
            print(False)
        else:
            print(format(ans, 'x'))

# Task 3, 4
def test34():
    print('\nTEST: Task 3, 4')
    controlLogic()
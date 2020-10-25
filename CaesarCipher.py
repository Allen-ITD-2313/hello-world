def cipher(code, distance):
    plainText = ""
    for ch in code:
        ordvalue = ord(ch)
        ciphervalue = ordvalue - distance
        if ciphervalue < ord('a'):
            ciphervalue = ord('z') - (distance - (ord('a')-ordvalue - 1))
        plainText += chr(ciphervalue)
    return plainText

code = input("enter coded text: ")
distance = int(input("enter value: "))
print(cipher(code, distance))

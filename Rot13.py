import unittest


def rot13(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    encoded = ""
    for x in range(len(message)):
        if message[x].lower() in alphabet:
            index = alphabet.index(message[x].lower()) + 13
            if index > (len(alphabet) - 1):
                index %= len(alphabet)
                if message[x].isupper():
                    encoded += alphabet[index].upper()
                else:
                    encoded += alphabet[index]
            else:
                if message[x].isupper():
                    encoded += alphabet[index].upper()
                else:
                    encoded += alphabet[index]
        else:
            encoded += message[x]
    return encoded

test.assert_equals(rot13(rot13("Test")),"Test")
print(rot13("Nibvq fhpprff ng nyy pbfgf!"))


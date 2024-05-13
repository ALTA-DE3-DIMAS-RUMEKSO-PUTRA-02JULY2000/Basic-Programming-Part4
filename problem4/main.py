def ubah_huruf(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = "KLMNOPQRSTUVWXYZABCDEFGHIJ"

    encrypted_sentence = ""

    for char in sentence:
        if char.isalpha() and char.isupper():
            index = alphabet.index(char)
            encrypted_char = shifted_alphabet[index]
            encrypted_sentence += encrypted_char
        else:
            encrypted_sentence += char

    return encrypted_sentence

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB
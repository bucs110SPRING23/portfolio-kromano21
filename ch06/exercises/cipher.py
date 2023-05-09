def main():
    message = caesarcipher("The quick brown fox jumps over the lazy dog", 3)
    encryptedoutput(message)

def caesarcipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A') 
            else:
                ord('a')
        if ord(char) > 13:
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        if ord(char) <= 13:
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        result += char
    return result

def encryptedoutput(message):
    file_pointer = open("output.txt", 'w')
    file_pointer.write(message)
    file_pointer.close()

main()






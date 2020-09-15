import argparse



def encrypt_file(fileName):
    # Reads the file to be encrypted and puts the lines of the file into a list
    with open(fileName) as f:
        lines = f.readlines()

    if lines[0] != "ENCRYPTED\n":

        encryptedLines = []
        # Iterates through the characters of the lines of the text file and substitutes each letter using a caesar cipher
        for line in lines:
            line = line.rstrip('\n')
            encryptedLine = ""
            for char in line:
                # last character 'z' has value 122, after that value weird characters appears
                if ord(char) > 112:
                    newCharNum = 96 + (10 - (122 - ord(char)))
                    newChar = chr(newCharNum)
                    encryptedLine += newChar
                # 32 == spacebar
                elif ord(char) == 32:
                    newCharNum = ord(char)
                    newChar = chr(newCharNum)
                    encryptedLine += newChar
                else:
                    newCharNum = ord(char) + 10
                    newChar = chr(newCharNum)
                    encryptedLine += newChar
            encryptedLines.append(encryptedLine + '\n')

        encryptedLines.insert(0, "ENCRYPTED\n")

        # Writes the newly encrypted lines to the file
        with open(fileName, 'w') as f:
            f.writelines(encryptedLines)
    else:
        print("Text file already encrypted.")



def decrypt_file(fileName):
    # Reads the file to be decrypted and puts the lines of the file into a list
    with open(fileName) as f:
        lines = f.readlines()

    if lines[0] == "ENCRYPTED\n":
        lines = lines[1:]

        decryptedLines = []
        # Iterates through the characters of the lines of the text file and substitutes each letter using a caesar cipher
        for line in lines:
            line = line.rstrip('\n')
            decryptedLine = ""
            for char in line:
                # 32 == spacebar
                if ord(char) == 32:
                    newCharNum = ord(char)
                    newChar = chr(newCharNum)
                    decryptedLine += newChar
                elif ord(char) < 107:
                    newCharNum =  123 - (10 - (ord(char) - 97))
                    newChar = chr(newCharNum)
                    decryptedLine += newChar
                else:
                    newCharNum = ord(char) - 10
                    newChar = chr(newCharNum)
                    decryptedLine += newChar
            decryptedLines.append(decryptedLine + '\n')

        # Writes the newly decrypted lines to the file 
        with open(fileName, 'w') as f:
            f.writelines(decryptedLines)
    else:
        print("Text file is not encrypted.")


parser = argparse.ArgumentParser(description='Encrypts/decrypts a text file')
parser.add_argument('--e', help="Encrypts the given text file")
parser.add_argument('--d', help="Decrypts the given text file")
args = parser.parse_args()

if (args.e):
    encrypt_file(args.e)
elif (args.d):
    decrypt_file(args.d)

import os as operating
import random
global sym1, sym2, sym3, sym4, sym5
sym1 = "##############################################################"
sym2 = "##############################################################"
sym3 = "##############################################################"
sym4 = "##############################################################"
sym5 = "##############################################################"
def encryption():
    encryption_algorithm = {
                " ": "-",
                "0": "7",
                "1": "3",
                "2": "5",
                "3": "6",
                "4": "8",
                "5": "1",
                "6": "2",
                "7": "4",
                "8": "9",
                "9": "0",
                "a": "&",
                "b": "*",
                "c": "$",
                "d": ".",
                "e": "~",
                "f": "!",
                "g": "@",
                "h": "#",
                "i": "%",
                "I": ")",
                "j": "+",
                "k": "(",
                "l": "[",
                "m": "}",
                "n": ";",
                "o": ":",
                "p": "/",
                "q": ">",
                "r": "|",
                "s": "<",
                "t": "]",
                "u": "=",
                "v": "_",
                "w": "'",
                "x": "^",
                "y": "{",
                "z": "?",
                }
    choice = "\n\twelcome to my encryption algorithm.\n"
    choice += "\tenter the sentence or word you would like to encrypt.\n"
    choice += "\tto go back type 'back'.\n"
    choice += "\ttype here => "
    reg_text = input(choice.title())
    if reg_text == "back" or reg_text == "Back":
        operating.system('cls')
        display()
    cipher_text = ""
    for letters in reg_text:
        if letters == 'A' or letters == 'a':
            cipher_text += encryption_algorithm['a']
        elif letters == 'B' or letters == 'b':
            cipher_text += encryption_algorithm['b']
        elif letters == 'C' or letters == 'c':
            cipher_text += encryption_algorithm['c']
        elif letters == 'D' or letters == 'd':
            cipher_text += encryption_algorithm['d']
        elif letters == 'E' or letters == 'e':
            cipher_text += encryption_algorithm['e']
        elif letters == 'F' or letters == 'f':
            cipher_text += encryption_algorithm['f']
        elif letters == 'G' or letters == 'g':
            cipher_text += encryption_algorithm['g']
        elif letters == 'H' or letters == 'h':
            cipher_text += encryption_algorithm['h']
        elif letters == 'i':
            cipher_text += encryption_algorithm['i']
        elif letters == 'I':
            cipher_text += encryption_algorithm['I']
        elif letters == 'J' or letters == 'j':
            cipher_text += encryption_algorithm['j']
        elif letters == 'K' or letters == 'k':
            cipher_text += encryption_algorithm['k']
        elif letters == 'L' or letters == 'l':
            cipher_text += encryption_algorithm['l']
        elif letters == 'M' or letters == 'm':
            cipher_text += encryption_algorithm['m']
        elif letters == 'N' or letters == 'n':
            cipher_text += encryption_algorithm['n']
        elif letters == 'O' or letters == 'o':
            cipher_text += encryption_algorithm['o']
        elif letters == 'P' or letters == 'p':
            cipher_text += encryption_algorithm['p']
        elif letters == 'Q' or letters == 'q':
            cipher_text += encryption_algorithm['q']
        elif letters == 'R' or letters == 'r':
            cipher_text += encryption_algorithm['r']
        elif letters == 'S' or letters == 's':
            cipher_text += encryption_algorithm['s']
        elif letters == 'T' or letters == 't':
            cipher_text += encryption_algorithm['t']
        elif letters == 'U' or letters == 'u':
            cipher_text += encryption_algorithm['u']
        elif letters == 'V' or letters == 'v':
            cipher_text += encryption_algorithm['v']
        elif letters == 'W' or letters == 'w':
            cipher_text += encryption_algorithm['w']
        elif letters == 'X' or letters == 'x':
            cipher_text += encryption_algorithm['x']
        elif letters == 'Y' or letters == 'y':
            cipher_text += encryption_algorithm['y']
        elif letters == 'Z' or letters == 'z':
            cipher_text += encryption_algorithm['z']
        elif letters == '0':
            cipher_text += encryption_algorithm['0']
        elif letters == '1':
            cipher_text += encryption_algorithm['1']
        elif letters == '2':
            cipher_text += encryption_algorithm['2']
        elif letters == '3':
            cipher_text += encryption_algorithm['3']
        elif letters == '4':
            cipher_text += encryption_algorithm['4']
        elif letters == '5':
            cipher_text += encryption_algorithm['5']
        elif letters == '6':
            cipher_text += encryption_algorithm['6']
        elif letters == '7':
            cipher_text += encryption_algorithm['7']
        elif letters == '8':
            cipher_text += encryption_algorithm['8']
        elif letters == '9':
            cipher_text += encryption_algorithm['9']
        elif letters == " ":
            cipher_text += encryption_algorithm[" "]
        else:
            continue
    leng = int(len(reg_text))
    join = sym1 + sym2 + sym3 + sym4 + sym5 
    leng2 = "".join(random.sample(join,leng))
    if leng == " ":
        print("-")
    print(f"\n\t##############################{leng2}")
    print(f"\tHere is the encrypted format: {cipher_text}", end="" + "\n")
    print(f"\t##############################{leng2}")
def decryption():
    text = "\n\twelcome to my decryption algorithm.\n"
    text += "\tto go back type 'back'\n"
    text += "\tenter the encrypted text you would like to decrypt => "
    encrypted_text = input(text.title())
    if encrypted_text == "back" or encrypted_text == "Back":
        operating.system('cls')
        display()
    decryption_algorithm = {
                "-": " ",
                "7": "0",
                "3": "1",
                "5": "2",
                "6": "3",
                "8": "4",
                "1": "5",
                "2": "6",
                "4": "7",
                "9": "8",
                "0": "9",
                "&": "a",
                "*": "b",
                "$": "c",
                ".": "d",
                "~": "e",
                "!": "f",
                "@": "g",
                "#": "h",
                "%": "i",
                ")": "I",
                "+": "j",
                "(": "k",
                "[": "l",
                "}": "m",
                ";": "n",
                ":": "o",
                "/": "p",
                ">": "q",
                "|": "r",
                "<": "s",
                "]": "t",
                "=": "u",
                "_": "v",
                "'": "w",
                "^": "x",
                "{": "y",
                "?": "z"
        }
    plain_text = ""
    for cipher_letters in encrypted_text:
        if cipher_letters == "&":
            plain_text += decryption_algorithm["&"]
        elif cipher_letters == "*":
            plain_text += decryption_algorithm["*"]
        elif cipher_letters == "$":
            plain_text += decryption_algorithm["$"]
        elif cipher_letters == ".":
            plain_text += decryption_algorithm["."]
        elif cipher_letters == "~":
            plain_text += decryption_algorithm["~"]
        elif cipher_letters == "!":
            plain_text += decryption_algorithm["!"]
        elif cipher_letters == "@":
            plain_text += decryption_algorithm["@"]
        elif cipher_letters == "#":
            plain_text += decryption_algorithm["#"]
        elif cipher_letters == "%":
            plain_text += decryption_algorithm["%"]
        elif cipher_letters == ")":
            plain_text += decryption_algorithm[")"]
        elif cipher_letters == "+":
            plain_text += decryption_algorithm["+"]
        elif cipher_letters == "(":
            plain_text += decryption_algorithm["("]
        elif cipher_letters == "[":
            plain_text += decryption_algorithm["["]
        elif cipher_letters == "}":
            plain_text += decryption_algorithm["}"]
        elif cipher_letters == ",":
            plain_text += decryption_algorithm[","]
        elif cipher_letters == ":":
            plain_text += decryption_algorithm[":"]
        elif cipher_letters == ";":
            plain_text += decryption_algorithm[";"]
        elif cipher_letters == "/":
            plain_text += decryption_algorithm["/"]
        elif cipher_letters == ">":
            plain_text += decryption_algorithm[">"]
        elif cipher_letters == "|":
            plain_text += decryption_algorithm["|"]
        elif cipher_letters == "<":
            plain_text += decryption_algorithm["<"]
        elif cipher_letters == "]":
            plain_text += decryption_algorithm["]"]
        elif cipher_letters == "=":
            plain_text += decryption_algorithm["="]
        elif cipher_letters == "_":
            plain_text += decryption_algorithm["_"]
        elif cipher_letters == "'":
            plain_text += decryption_algorithm["'"]
        elif cipher_letters == "^":
            plain_text += decryption_algorithm["^"]
        elif cipher_letters == "{":
            plain_text += decryption_algorithm["{"]
        elif cipher_letters == "?":
            plain_text += decryption_algorithm["?"]
        elif cipher_letters == "-":
            plain_text += decryption_algorithm["-"]
        elif cipher_letters == "7":
            plain_text += decryption_algorithm["7"]
        elif cipher_letters == "3":
            plain_text += decryption_algorithm["3"]
        elif cipher_letters == "5":
            plain_text += decryption_algorithm["5"]
        elif cipher_letters == "6":
            plain_text += decryption_algorithm["6"]
        elif cipher_letters == "8":
            plain_text += decryption_algorithm["8"]
        elif cipher_letters == "1":
            plain_text += decryption_algorithm["1"]
        elif cipher_letters == "2":
            plain_text += decryption_algorithm["2"]
        elif cipher_letters == "4":
            plain_text += decryption_algorithm["4"]
        elif cipher_letters == "9":
            plain_text += decryption_algorithm["9"]
        elif cipher_letters == "0":
            plain_text += decryption_algorithm["0"]
    leng = int(len(encrypted_text))
    join = sym1 + sym2 + sym3 + sym4 + sym5 
    leng2 = "".join(random.sample(join,leng))
    if leng == "-":
        print(" ")
    print(f"\n\t##############################{leng2}")
    print(f"\tHere is the decrypted format: {plain_text}", end="" + "\n")
    print(f"\t##############################{leng2}")
def display():
    operating.system('color e')
    user_choice = "\n\tto encrypt type 'c'\n"
    user_choice += "\tto decrypt type 'p' \n"
    user_choice += "\tto exit type 'bye'\n"
    user_choice += "\tenter option here >> "
    while user_choice:
        answer = input(user_choice.swapcase())
        if answer == "cipher" or answer == "CIPHER" or answer == "C" or answer == "c":
            encryption()
        elif answer == "plain" or answer == "PLAIN" or answer == "P" or answer == "p":
            decryption()
        elif answer == "bye" or answer == "BYE" or answer == "Bye":
            break
        else:
            operating.system('cls')
            print("\tInvalid option, try again.")
            display()
display()
# reverse the dictionary
# reverse = dict()
# for key in encryption_algorithm2:
#    value = encryption_algorithm2[key]
#    reverse[value] = key
# reverse is the encryption_algorithm dict in reverse
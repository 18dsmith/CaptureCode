from PIL import Image
from base64 import b64decode
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

class Char:
    def __init__(self, instructions, colour, text):
        self.instructions = instructions
        self.colour = colour
        self.text = text

character_list = []

#BLACK (0, 0, 0)
character_list.append(Char([0, 0, 0, 0], (0, 0, 0), "0")) # 0
character_list.append(Char([1, 0, 0, 0], (0, 0, 0), "1")) # 1
character_list.append(Char([0, 1, 0, 0], (0, 0, 0), "2")) # 2
character_list.append(Char([0, 0, 1, 0], (0, 0, 0), "3")) # 3
character_list.append(Char([0, 0, 0, 1], (0, 0, 0), "4")) # 4
character_list.append(Char([1, 1, 0, 0], (0, 0, 0), "5")) # 5
character_list.append(Char([1, 0, 1, 0], (0, 0, 0), "6")) # 6
character_list.append(Char([1, 0, 0, 1], (0, 0, 0), "7")) # 7
character_list.append(Char([0, 1, 1, 0], (0, 0, 0), "8")) # 8
character_list.append(Char([0, 1, 0, 1], (0, 0, 0), "9")) # 9
character_list.append(Char([0, 0, 1, 1], (0, 0, 0), "A")) # A 10
character_list.append(Char([1, 1, 1, 0], (0, 0, 0), "B")) # B 11
character_list.append(Char([1, 1, 0, 1], (0, 0, 0), "C")) # C 12
character_list.append(Char([1, 0, 1, 1], (0, 0, 0), "D")) # D 13
character_list.append(Char([0, 1, 1, 1], (0, 0, 0), "E")) # E 14
character_list.append(Char([1, 1, 1, 1], (0, 0, 0), "F")) # F 15

#SPECIAL (255, 0, 0)
character_list.append(Char([1, 1, 1, 1], (255, 255, 0), "G")) # G 16

#RED (255, 0, 0)
character_list.append(Char([1, 0, 0, 0], (255, 0, 0), "H")) # H 17
character_list.append(Char([0, 1, 0, 0], (255, 0, 0), "I")) # I 18
character_list.append(Char([0, 0, 1, 0], (255, 0, 0), "J")) # J 19
character_list.append(Char([0, 0, 0, 1], (255, 0, 0), "K")) # K 20
character_list.append(Char([1, 1, 0, 0], (255, 0, 0), "L")) # L 21
character_list.append(Char([1, 0, 1, 0], (255, 0, 0), "M")) # M 22
character_list.append(Char([1, 0, 0, 1], (255, 0, 0), "N")) # N 23
character_list.append(Char([0, 1, 1, 0], (255, 0, 0), "O")) # O 24
character_list.append(Char([0, 1, 0, 1], (255, 0, 0), "P")) # P 25
character_list.append(Char([0, 0, 1, 1], (255, 0, 0), "Q")) # Q 26
character_list.append(Char([1, 1, 1, 0], (255, 0, 0), "R")) # R 27
character_list.append(Char([1, 1, 0, 1], (255, 0, 0), "S")) # S 28
character_list.append(Char([1, 0, 1, 1], (255, 0, 0), "T")) # T 29
character_list.append(Char([0, 1, 1, 1], (255, 0, 0), "U")) # U 30
character_list.append(Char([1, 1, 1, 1], (255, 0, 0), "V")) # V 31

#SPECIAL (0, 255, 0)
character_list.append(Char([1, 1, 1, 1], (255, 0, 255), "W")) # W 32

#GREEN (0, 255, 0)
character_list.append(Char([1, 0, 0, 0], (0, 255, 0), "X")) # X 33
character_list.append(Char([0, 1, 0, 0], (0, 255, 0), "Y")) # Y 34
character_list.append(Char([0, 0, 1, 0], (0, 255, 0), "Z")) # Z 35
character_list.append(Char([0, 0, 0, 1], (0, 255, 0), "a")) # a 36
character_list.append(Char([1, 1, 0, 0], (0, 255, 0), "b")) # b 37
character_list.append(Char([1, 0, 1, 0], (0, 255, 0), "c")) # c 38
character_list.append(Char([1, 0, 0, 1], (0, 255, 0), "d")) # d 39
character_list.append(Char([0, 1, 1, 0], (0, 255, 0), "e")) # e 40
character_list.append(Char([0, 1, 0, 1], (0, 255, 0), "f")) # f 41
character_list.append(Char([0, 0, 1, 1], (0, 255, 0), "g")) # g 42
character_list.append(Char([1, 1, 1, 0], (0, 255, 0), "h")) # h 43
character_list.append(Char([1, 1, 0, 1], (0, 255, 0), "i")) # i 44
character_list.append(Char([1, 0, 1, 1], (0, 255, 0), "j")) # j 45
character_list.append(Char([0, 1, 1, 1], (0, 255, 0), "k")) # k 46
character_list.append(Char([1, 1, 1, 1], (0, 255, 0), "l")) # l 47

#SPECIAL (0, 0, 255)
character_list.append(Char([1, 1, 1, 1], (0, 255, 255), "m")) # m 48

#BLUE (0, 0, 255)
character_list.append(Char([1, 0, 0, 0], (0, 0, 255), "n")) # n 49
character_list.append(Char([0, 1, 0, 0], (0, 0, 255), "o")) # o 50
character_list.append(Char([0, 0, 1, 0], (0, 0, 255), "p")) # p 51
character_list.append(Char([0, 0, 0, 1], (0, 0, 255), "q")) # q 52
character_list.append(Char([1, 1, 0, 0], (0, 0, 255), "r")) # r 53
character_list.append(Char([1, 0, 1, 0], (0, 0, 255), "s")) # s 54
character_list.append(Char([1, 0, 0, 1], (0, 0, 255), "t")) # t 55
character_list.append(Char([0, 1, 1, 0], (0, 0, 255), "u")) # u 56
character_list.append(Char([0, 1, 0, 1], (0, 0, 255), "v")) # v 57
character_list.append(Char([0, 0, 1, 1], (0, 0, 255), "w")) # w 58
character_list.append(Char([1, 1, 1, 0], (0, 0, 255), "x")) # x 59
character_list.append(Char([1, 1, 0, 1], (0, 0, 255), "y")) # y 60
character_list.append(Char([1, 0, 1, 1], (0, 0, 255), "z")) # z 61
character_list.append(Char([0, 1, 1, 1], (0, 0, 255), "/")) # / 62
character_list.append(Char([1, 1, 1, 1], (0, 0, 255), "+")) # + 63

def convert_to_string(count):
    colour = (0, 0, 0)
    char_instructions = []
    for i in range(4):
        y = float((count / 20))
        y = int((y))
        y *= 2
        x = (i % 2) + (2 * count)
        x -= y*20
        if i >= 2:
            y += 1
        if pixels[x, y] != (255, 255, 255):
            char_instructions.append(1)
            r, g, b = char_image.getpixel((x, y))
            colour = (r, g, b)
        else:
            char_instructions.append(0)
    char_instructions.append(colour)
    instruction_list.append(char_instructions)

name = input("Enter title of saved code.\n> ")
name += ".png"
try:
    char_image = Image.open(name)
except:
    input(f"Error: Unable to find file {name}\nPossible fix: Check your spelling of the filename.\nPress <ENTER> to close.")
    exit()

pixels = char_image.load()
instruction_list = []
count = 0
for i in range(342):
    convert_to_string(count)
    count += 1

string_new = ""
for instruction in instruction_list:
    for char in character_list:
        if char.instructions == instruction[:-1] and char.colour == instruction[4]:
            string_new += char.text
extra = 4 - (len(string_new) % 4)
if extra != 4:
    string_new += extra * "="

try:
    privkey = open('private.pem','r').read()
except FileNotFoundError:
    input("Error: No keys found.\nPossible fix: Run key_gen.py file.\nPress <ENTER> to close.")
    exit()
    
private_key = RSA.importKey(privkey)
decryptor = PKCS1_v1_5.new(private_key)
string_new = b64decode(string_new)
decrypted = decryptor.decrypt(string_new, "error")
decrypted = decrypted.decode('utf-8')
print('Decrypted:', decrypted)
if len(decrypted) == 0:
    print("Hmm, that's a short message. Are you using the same public/private keys as when you generated it?")
input("Press <ENTER> to close.")
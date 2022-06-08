from PIL import Image
from base64 import b64encode
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

class Char:
    def __init__(self, instructions, colour):
        self.instructions = instructions
        self.colour = colour


    def convert_to_symbol(self, count):
        for i in range(len(self.instructions)):
            y = float((count / 20))
            y = int((y))
            y *= 2
            x = (i % 2) + (2 * count)
            x -= y*20
            if i >= 2:
                y += 1
            if self.instructions[i] == 0:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = self.colour


character_list = []

#BLACK (0, 0, 0)
character_list.append(Char([0, 0, 0, 0], (0, 0, 0))) # 0
character_list.append(Char([1, 0, 0, 0], (0, 0, 0))) # 1
character_list.append(Char([0, 1, 0, 0], (0, 0, 0))) # 2
character_list.append(Char([0, 0, 1, 0], (0, 0, 0))) # 3
character_list.append(Char([0, 0, 0, 1], (0, 0, 0))) # 4
character_list.append(Char([1, 1, 0, 0], (0, 0, 0))) # 5
character_list.append(Char([1, 0, 1, 0], (0, 0, 0))) # 6
character_list.append(Char([1, 0, 0, 1], (0, 0, 0))) # 7
character_list.append(Char([0, 1, 1, 0], (0, 0, 0))) # 8
character_list.append(Char([0, 1, 0, 1], (0, 0, 0))) # 9
character_list.append(Char([0, 0, 1, 1], (0, 0, 0))) # A 10
character_list.append(Char([1, 1, 1, 0], (0, 0, 0))) # B 11
character_list.append(Char([1, 1, 0, 1], (0, 0, 0))) # C 12
character_list.append(Char([1, 0, 1, 1], (0, 0, 0))) # D 13
character_list.append(Char([0, 1, 1, 1], (0, 0, 0))) # E 14
character_list.append(Char([1, 1, 1, 1], (0, 0, 0))) # F 15

#SPECIAL (255, 0, 0)
character_list.append(Char([1, 1, 1, 1], (255, 255, 0))) # G 16

#RED (255, 0, 0)
character_list.append(Char([1, 0, 0, 0], (255, 0, 0))) # H 17
character_list.append(Char([0, 1, 0, 0], (255, 0, 0))) # I 18
character_list.append(Char([0, 0, 1, 0], (255, 0, 0))) # J 19
character_list.append(Char([0, 0, 0, 1], (255, 0, 0))) # K 20
character_list.append(Char([1, 1, 0, 0], (255, 0, 0))) # L 21
character_list.append(Char([1, 0, 1, 0], (255, 0, 0))) # M 22
character_list.append(Char([1, 0, 0, 1], (255, 0, 0))) # N 23
character_list.append(Char([0, 1, 1, 0], (255, 0, 0))) # O 24
character_list.append(Char([0, 1, 0, 1], (255, 0, 0))) # P 25
character_list.append(Char([0, 0, 1, 1], (255, 0, 0))) # Q 26
character_list.append(Char([1, 1, 1, 0], (255, 0, 0))) # R 27
character_list.append(Char([1, 1, 0, 1], (255, 0, 0))) # S 28
character_list.append(Char([1, 0, 1, 1], (255, 0, 0))) # T 29
character_list.append(Char([0, 1, 1, 1], (255, 0, 0))) # U 30
character_list.append(Char([1, 1, 1, 1], (255, 0, 0))) # V 31

#SPECIAL (0, 255, 0)
character_list.append(Char([1, 1, 1, 1], (255, 0, 255))) # W 32

#GREEN (0, 255, 0)
character_list.append(Char([1, 0, 0, 0], (0, 255, 0))) # X 33
character_list.append(Char([0, 1, 0, 0], (0, 255, 0))) # Y 34
character_list.append(Char([0, 0, 1, 0], (0, 255, 0))) # Z 35
character_list.append(Char([0, 0, 0, 1], (0, 255, 0))) # a 36
character_list.append(Char([1, 1, 0, 0], (0, 255, 0))) # b 37
character_list.append(Char([1, 0, 1, 0], (0, 255, 0))) # c 38
character_list.append(Char([1, 0, 0, 1], (0, 255, 0))) # d 39
character_list.append(Char([0, 1, 1, 0], (0, 255, 0))) # e 40
character_list.append(Char([0, 1, 0, 1], (0, 255, 0))) # f 41
character_list.append(Char([0, 0, 1, 1], (0, 255, 0))) # g 42
character_list.append(Char([1, 1, 1, 0], (0, 255, 0))) # h 43
character_list.append(Char([1, 1, 0, 1], (0, 255, 0))) # i 44
character_list.append(Char([1, 0, 1, 1], (0, 255, 0))) # j 45
character_list.append(Char([0, 1, 1, 1], (0, 255, 0))) # k 46
character_list.append(Char([1, 1, 1, 1], (0, 255, 0))) # l 47

#SPECIAL (0, 0, 255)
character_list.append(Char([1, 1, 1, 1], (0, 255, 255))) # m 48

#BLUE (0, 0, 255)
character_list.append(Char([1, 0, 0, 0], (0, 0, 255))) # n 49
character_list.append(Char([0, 1, 0, 0], (0, 0, 255))) # o 50
character_list.append(Char([0, 0, 1, 0], (0, 0, 255))) # p 51
character_list.append(Char([0, 0, 0, 1], (0, 0, 255))) # q 52
character_list.append(Char([1, 1, 0, 0], (0, 0, 255))) # r 53
character_list.append(Char([1, 0, 1, 0], (0, 0, 255))) # s 54
character_list.append(Char([1, 0, 0, 1], (0, 0, 255))) # t 55
character_list.append(Char([0, 1, 1, 0], (0, 0, 255))) # u 56
character_list.append(Char([0, 1, 0, 1], (0, 0, 255))) # v 57
character_list.append(Char([0, 0, 1, 1], (0, 0, 255))) # w 58
character_list.append(Char([1, 1, 1, 0], (0, 0, 255))) # x 59
character_list.append(Char([1, 1, 0, 1], (0, 0, 255))) # y 60
character_list.append(Char([1, 0, 1, 1], (0, 0, 255))) # z 61
character_list.append(Char([0, 1, 1, 1], (0, 0, 255))) # / 62
character_list.append(Char([1, 1, 1, 1], (0, 0, 255))) # + 63

char_image = Image.new('RGB', (40, 40), 'white')

pubkey = open('receiver.pem','r').read()
msg = input("Message\n> ").encode('utf-8')
public_key = RSA.importKey(pubkey)
cipher = PKCS1_v1_5.new(public_key)
new_msg = cipher.encrypt(msg)
new_msg = b64encode(new_msg)
new_msg = new_msg.decode('utf-8')

string_new = []
string_count = 0
count = 0
for char in new_msg:
    try:
        char = int(char)
        string_new.append(char)
    except:
        if char == "/":
            string_new.append(62)
        elif char == "+":
            string_new.append(63)
        elif char == "=":
            pass
        elif char.upper() == char:
            string_new.append((ord(char.lower()) - 97) + 10)
        else:
            string_new.append((ord(char) - 97) + 36)

pixels = char_image.load()
for num in string_new:
    try:
        character_list[num].convert_to_symbol(count)
        count += 1
    except:
        print(num)

char_image.save('CODE.png')
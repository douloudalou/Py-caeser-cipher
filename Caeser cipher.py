# Allows choosing of Encrypt or Decrypt 
# Able to work with spaces " "
# Password function

from time import sleep

Encrypt_Decrypt = input("Encrypt or Decrypt: ")
Type = input("Type: ")
Text = input("Text: ").lower()
new_text = []
smt = []
num_tries = 0
Access = False
Alphabets = "abcdefghijklmnopqrstuvwxyz"

def checking_password(x):
    print(x)
    if x == 1:
        print("First try")
    elif x == 2:
        print("Second try")
    elif x == 3:
        print("Third try")
    password = input("Password: ")
    print("Checking password")
    
    if x < 3:
        if Encrypt_Decrypt == "Encrypt":
            if password == "123":
                Access = True
                main(Access)
            else:
                print("Wrong Password")
                checking_password(x+1)
        elif Encrypt_Decrypt == "Decrypt":
            if password == "321":
                Access = True
                main(Access)
            else:
                print("Wrong Password")
                checking_password(x+1)
    elif x >= 3:
        print("U sure u the Owner???")
        print("Cuz I dun think so")
        print("so no tries for 10sec")
        sleep(10)
        x = 1
        checking_password(x)
        
def Encrypt(c):
    char_index = Alphabets.index(c)
    new_char_index = 0
    new_char = ""

    if Type == "Normal":
        new_char_index = (char_index + 3) % len(Alphabets)
        new_char = Alphabets[new_char_index]
    elif Type == "Meee":
        breakpoint

    new_text.append(new_char)

def Decrypt(c):
    char_index = Alphabets.index(c)
    new_char_index = 0
    new_char = ""

    if Type == "Normal":
        new_char_index = (char_index - 3) % len(Alphabets)
        new_char = Alphabets[new_char_index]
    elif Type == "Meee":
        breakpoint

    new_text.append(new_char)

def print_text():
    print_text = ""
    for x in new_text:
        if x == "###":
            x = " "
        print_text += x
    print(print_text)

def main(Access):
    if Access == False:
        x = 1
        checking_password(x)
    elif Access == True:
        for c in Text:
            if c == " ":
                c = "###"
                smt.append(c)
            else:
                smt.append(c)

        for c in smt:
            if c == "###":
                new_text.append(c)
            else:
                if Encrypt_Decrypt == "Encrypt":
                    Encrypt(c)
                elif Encrypt_Decrypt == "Decrypt":
                    Decrypt(c)

        print_text()
        print("Done encrypting")

main(Access)
#Secret message 

def encode():
    
    if (m == 1):
        c1()
    elif (m == 2):
        c2()
    elif (m == 3):
        c3()
    elif (m == 4):
        c4()
    elif (m == 5):
        c5()
    elif (m == 6):
        c6()
    elif (m == 7):
        c7()
    elif (m == 8):
        c8()
    else:
        c9()
        
def decode():
    
    if (m == 1):
        d1()
    elif (m == 2):
        d2()
    elif (m == 3):
        d3()
    elif (m == 4):
        d4()
    elif (m == 5):
        d5()
    elif (m == 6):
        d6()
    elif (m == 7):
        d7()
    elif (m == 8):
        d8()
    else:
        d9()
    
def c1():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+n+o)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d1():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-n-o)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c2():
    newmessage = ''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+o)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d2():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-p-o)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c3():
    newmessage = ''
    
    for character in message:       
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position-p-o)%62
            if(newposition < 0):
                newposition += 62
            newcharacter = alphabet[newposition]
            newmessage = newmessage + newcharacter
        else:
            newmessage = newmessage + character
    print('encrypted code is : ', newmessage)
    
def d3():
    newmessage = ''
    
    for character in message:    
        if character in alphabet:
            position = alphabet.find(character)            
            newposition = (position+p+o)%62
            newcharacter = alphabet[newposition]
            newmessage = newmessage + newcharacter
        else:
            newmessage = newmessage + character
    print('decrypted code is : ', newmessage)
    
def c4():
    newmessage = ''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position-n-o)%62
            if(newposition<0):
                newposition += 62
            newcharacter = alphabet[newposition]
            newmessage = newmessage + newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d4():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+o+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c5():
    newmessage = ''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position-p-n)%62
            if(newposition<0):
                newposition += 62
            newcharacter = alphabet[newposition]
            newmessage = newmessage + newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d5():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c6():
    newmessage = ''
    alphabet = 'qwertyuiopasdfghjklzxcvbnm1357924680QWERTYUIOPASDFGHJKLZXCVBNM'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+o+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d6():
    newmessage=''
    alphabet='qwertyuiopasdfghjklzxcvbnm1357924680QWERTYUIOPASDFGHJKLZXCVBNM'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-p-o-n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c7():
    newmessage = ''
    alphabet = 'zxcvbnmasdfghjklqwertyuiop2468013579ZXCVBNMASDFGHJKLQWERTYUIOP'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+o+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d7():
    newmessage = ''
    alphabet = 'zxcvbnmasdfghjklqwertyuiop2468013579ZXCVBNMASDFGHJKLQWERTYUIOP'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-p-o-n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)
    
def c8():
    newmessage = ''
    qwerty = '1357924680qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+o+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d8():
    newmessage = ''
    qwerty = '1357924680qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-p-o-n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)

def c9():
    newmessage = ''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+p+n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('encrypted code is : ', newmessage)
    
def d9():
    newmessage=''
    
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position+62-p-n)%62
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    print('decrypted code is : ', newmessage)

    
print('Welcome to secret message where u can secure your message!\n')
ch = 'yes'
while ch == 'yes':
    
    c = input("Press 1. for Encryption and else for Decryption : ")

    

    while True:
        key = input("Please enter a 4 digit key : ")
        

        
        for i in key:

            if ord(i) > 47 and ord(i) < 58:
                true = 1
            else:
                true = 0
                break
        if true == 1:
            if(int(key) > 999 and int(key) < 10000):
                m = int(key[0])
                n = int(key[1])
                o = int(key[2])
                p = int(key[3])
                break
            else:
                print("Enter key in range(1000,9999)")
        else:
            print('Enter an integer key only!')
        
    message = input("Enter the message : ")

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if (c == '1'):
        encode()
    else:
        decode()

    print('Do you want to encrypt or decrypt more messages?(yes/no)')
    ch = input().lower()
    print('\n')
    

    






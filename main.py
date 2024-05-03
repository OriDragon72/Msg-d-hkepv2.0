from DHKEPv1 import Master_C0De
import os

def A2B(string):
    a = ""
    for char in string:
        binary_char = bin(ord(char))[2:].zfill(8)
        a += binary_char
    return a

def B2A(binary_code):
    b = ""
    for i in range(0, len(binary_code), 8):
        b += chr(int(binary_code[i:i+8], 2))
    return b

def xor_encrypt(message, key):
    encrypted_message = ""
    key_length = len(key)
    key_index = 0
    
    for char in message:
        encrypted_char = chr(ord(char) ^ ord(key[key_index]))
        encrypted_message += encrypted_char
        
        key_index = (key_index + 1) % key_length
        
    return encrypted_message

def main():
  os.system("clear")
  print("Welcome to the 'Msg-d-hkepv2.0'!")
  print("Would you like to encrypt or decrpt?")
  ans = input("[e/d]: ")
  if ans == "e":
    #get the message
    inp = input("Enter the message you want to encrypt: ")
    #message -> binary
    INP = A2B(inp)
    #generate key
    key = Master_C0De("A")
    #Key -> binary
    KEY = A2B(str(key))
  
    os.system("clear")

    print("Message provided[Original]: " + inp)
    print("Message[Binary]: " + INP)
    print("Key generated[Original]: " + str(key))
    print("Key[Binary]: " + KEY)

    xor = xor_encrypt(inp, str(key))
    
    print("Encrypted message[ASCII]: " + xor)
    print("Emcrypted Message[Binary]: " + A2B(xor))
    
  elif ans == "d":
    #get the message
    inp = input("Enter the message you want to decrypt: ")
    ANS = input("Was it in ASCII or Binary format? [a/b]: ")
    if ANS == "a":
      #message -> binary
      INP = A2B(inp)
    elif ANS == "b":
      INP = inp

  
    key = input("Enter the key used to encrypt the message: ")
    ANS = input("Was it in ASCII or Binary format? [a/b]: ")
    if ANS == "a":
      #message -> binary
      KEY = A2B(str(key))
    elif ANS == "b":
      KEY = key

    os.system("clear")

    print("Message provided: " + inp)
    print("Key provided: " + KEY)

    xor = xor_encrypt(inp, str(KEY))

    print("Decrypted message[ASCII]: " + xor)
    print("Decrypted Message[Binary]: " + A2B(xor))
    
main()
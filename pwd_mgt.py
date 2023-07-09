
from Crypto.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import hashlib
import json
import os

#----------------------------- Start Define Function -------------------------------

def show_menu():
    print("----------------------------------------")
    print("       Password Manager Program     ")
    print("     Please select menu from list     ")
    print("----------------------------------------")
    print("Type < 1 > to Stored Username & password")
    print("Tupe < 2 > to Show Username & password")
    print("Type < 3 or high > to Close program")
    print("----------------------------------------\n")

#function of hash sha256
def hash_sha256(txt):
    sha256 = hashlib.sha256()
    sha256.update(txt.encode('utf-8'))
    return sha256.digest()

def encode_password(username,key,text):
    
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    listObj = []

    #Data to be written
    data_json = {
        "username": username,
        "gmail_password": cipher_text.decode('latin-1')
    }

    #Check file already exists
    path = 'master_password.json'
    isFile = os.path.exists(path)

    if(isFile):
        # Append json data to list
        with open("master_password.json", "r") as file:
            listObj = json.load(file)
            print(listObj)
            listObj.append(data_json)

        # Serializing json
        with open("master_password.json", "w") as jsonfile:
            
            json.dump(listObj, jsonfile, indent=4, separators=(',',': '))
            print("\nSaved!")
            print("--------------------------------------------------")
            print("\\\\\\\\\\\\\\\\\\\\\\\ END //////////////////////")
            print("--------------------------------------------------\n")
    else:
        with open("master_password.json", "w") as jsonfile:
            json.dump(listObj, jsonfile, indent=4)

        # Append json data to list
        with open("master_password.json", "r") as file:
            listObj = json.load(file)
            print(listObj)
            listObj.append(data_json)

        # Serializing json
        with open("master_password.json", "w") as jsonfile:
            
            json.dump(listObj, jsonfile, indent=4, separators=(',',': '))
            print("\nSaved!")
            print("--------------------------------------------------")
            print("\\\\\\\\\\\\\\\\\\\\\\\ END //////////////////////")
            print("--------------------------------------------------\n")
        

def decode_password(username,key):

    with open("master_password.json", "r") as file:
        data = json.load(file)

        IsUser = False
        for i in range(len(data)):
            if data[i]['username'] == username:
                IsUser = True
                break
        if IsUser == True:
            try:
                cipher = AES.new(key, AES.MODE_ECB)
                plain_text = unpad(cipher.decrypt(data[i]['gmail_password'].encode('latin-1')), AES.block_size)
                print("\n*********************************")
                print('Gmail password is : ',plain_text.decode('utf-8'))
                print("*********************************\n")
            except (ValueError):
                print("\n*********************************")
                print("Master password isn't correct")
                print("*********************************\n")
            
            print("--------------------------------------------------")
            print("\\\\\\\\\\\\\\\\\\\\\\\ END //////////////////////")
            print("--------------------------------------------------\n")
        else:
            print("\n*********************************")
            print("!!! No have user !!!")
            print("*********************************\n")
                
                
#----------------------------- End Define Function -------------------------------


menu = 0
master = ''
key = ''

while menu < 3:

    #Call show_menu function for show menu
    show_menu()

    menu = int(input("Please select menu : "))

    if menu == 1:

        #input username & master password function
        username = input("PLease input username : ")
        master = input("PLease input master password : ")
        key = hash_sha256(master)
        
        text = input("Your gmail password : ")

        encode_password(username,key,text)

    elif menu == 2:

        #input username & master password function
        username = input("PLease input username : ")
        master = input("PLease input master password : ")
        key = hash_sha256(master)

        decode_password(username,key)
    
    elif menu >= 3:
        break






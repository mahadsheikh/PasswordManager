from cryptography.fernet import Fernet  # using this to encrypt the master password


pwd = input("what is the master password? : ") # needed to encrypt the password that we save in the file


def load_key(): # used to read the key once written
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

# key = load_key()
# functions to encrypt and decrypt passwords for us
def write_key(): # this specific functions will be used to generate and save a key that we will later use to encrypt and decrypt (one time use only)
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

# write_key()     this was only used once to make the file that was for the key


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            # print(line.rstrip()) # strips the extra line that is being used to save the password
            data = line.rstrip() #this return a list of string so we split it and use the elements in it
            usr,passw = data.split("|")
            print("Account Name : ",usr,", Password : ",passw)


def add():
    name = input("Account Name : ")
    pwd = input("Password: ")

    # file = open('password.txt','a') #when we open files like this then we have to manually close them 
    # file.close()

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Add Password or View existing password ?  (view,add) (q to quit): ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")
        continue


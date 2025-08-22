pwd = input("what is the master password? : ") # needed to encrypt the password

def view():
    pass

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


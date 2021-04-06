# register:
# username, email and password
# gnerate user id


# login:
# [username or email] and password

# bank operations



# init system 
# from random import randrang
import random
import datetime
dateTime = datetime.datetime.now()

database = {} #help to store user info
Moneydb = {"MONEY": 0} #help in storing money
complaindb = {} #store user complain for future refrence


def init():
    isvalidOptionSelected = False
    print("welcome to bankPHP")
    while isvalidOptionSelected == False:
        haveAccount = int(input("do you have accoumt with us: 1 (yes), 2 (no)\n"))
        if haveAccount == 1:
            isvalidOptionSelected = True
            login()
        elif haveAccount == 2:
            isvalidOptionSelected = True
            register()
        
        else:
            print("you have selected an invalid section")
        
# LOGING FOR EXISTING USER
def login():
    print("*******Login********")
    Id = int(input("whats your account number \n"))
    password = input("Enter your password\n").lower()
    for accountNumber,userPass in database.items(): 
        if  Id == accountNumber:
            if userPass[4]== password:
                print("Login Sucessful")
                # print(dateTime)
                bankOperation(userPass) 
    # print("invalid account or pass")    
        
    login()

# CREATING NEW USERS    
def register():
    print("*******New Account********")
    SureName = input("Enter Your Surname \n").lower()
    MiddleName = input("Enter Your Middle Name \n").lower()
    LastName = input("Enter Your Last Name \n").lower()
    email = input("Enter your email address \n").lower()
    
    generationAccountNumber()
    password = input("Create password \n")
    accountNumber = generationAccountNumber()
    database[accountNumber] = [SureName, MiddleName, LastName, email, password]
    print("Your account number is: ", accountNumber)
    login()
    
# USER ACTIVITIES    
def bankOperation(user):
    
    print("Welcome", (user[0], user[2]), dateTime)
    print("Your Balance is: ", Moneydb)
    print("This are options Avaliable")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Balance")
    print("4. Complaint")
    print("5. Exit")
    seletedOption = int(input("Please Select an Option: \n"))
        
        
    if (seletedOption == 1):
        print("You Select Option ", seletedOption)
        Q = int(input("Do you Have Want To Create OTWP? 1(yes) 3(No) \n"))
        if Q == 1:
            OTWP()
            OTP = OTWP()
            database = [OTP]
            print("Your OTWP is: ", OTP)
            USEROTWP = int(input("Enter your OTWP \n"))
            for USEROTWP in database:
                print(Moneydb)
                withdraw = int(input("How Much Do You Wish To Withdraw: \n"))
                if Moneydb["MONEY"] > withdraw:
                   withdraw1 = Moneydb["MONEY"] - withdraw 
                   Moneydb["MONEY"] = Moneydb["MONEY"] - withdraw
                   print("Transaction Sucessful Balance: ", Moneydb)
                
                
                else:
                    print("insuficient Funds")
                    print(Moneydb)
                        
        else:
            print("Have a nice day")
            exit()
            
                        
                        
            
    
    elif(seletedOption == 2):
        print("You Select Option ", seletedOption)
        Moneyinput = int(input("How Much Do You Wish To Deposit: \n"))
        Moneyinput = Moneydb["MONEY"] + Moneyinput
        Moneydb["MONEY"] = Moneydb["MONEY"] + Moneyinput
        print("Deposit was Sucessful!!!")
        print(Moneydb)
        
        
    elif (seletedOption == 3):
        print("You Select Option ", seletedOption)
        print("Balance: ", Moneydb)
        
               
    elif (seletedOption == 4):
        print("You Select Option ", seletedOption)
        response = input("What issue will you like to report? \n")
        response.append(complaindb)
        print("Thank you for contacting us")
        exit()
        
    elif (seletedOption == 5):
        print("You Select Option ", seletedOption)
        exit()
        
    else:
        print("Invalid Option, Please Try Again")
        
print("some operation")

# ONE TIMW WITHDRAWER PASSWORD GENERATION    
def OTWP():
    return random.randrange(11111,99999)
    # print("sucess")
    
# GENERATE ACCOUNT NUMBER
def generationAccountNumber():

    return random.randrange(1111111111,9999999999)
   
# USER DEPOSIT   
def deposite():
    print("Balance Befor Deposit: ", Moneydb)
    deposit = int(input("How Much Do You Wish To Deposit: \n"))
    deposit1 = Moneydb["MONEY"] + deposit
    Moneydb["MONEY"] = Moneydb["MONEY"] + deposit
    print("Deposit was Sucessful!!!")
    print("Balance After Deposit: ", Moneydb)
    d = int(input("do you want to perform another transaction? 1(yes), 2(no)\n"))
    if d == 2:
        exit()
    else:
        login()
        

    
def logout():
    exit()
    
###ACTUAL BANKING SYSTEM###
init()
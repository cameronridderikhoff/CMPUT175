#CMPUT 175
#Cameron Ridderikhoff
#Lab 2 exercise 1: Accounts
#Jan 26, 2017
def main():
#try to read the data  
    try:
        file = open("accounts.txt", "r")
        longstring = file.read()
        lines = longstring.splitlines()
        file.close() 
        accounts = {}
        #create the accounts
        for line in lines:
            account=line.split(":")
            try:
                account[1]=float(account[1])
                accounts[account[0]]=account[1]
            except ValueError: #if the value inside the account is not a float
                print("Account for "+str(account[0])+" not added: illegal value for balance")
                
        #get user input        
        uinput=input("Enter account name, or 'Stop' to exit: ")
        while uinput.upper() != "STOP":
            if uinput in accounts.keys():
                numinput = input("Enter transaction amount: ")
                try:
                    accounts[uinput] += float(numinput)
                    print("New balance for account "+str(uinput)+ " %.2f" % accounts[uinput])
                except ValueError:
                    print("Illegal value for transaction, transaction canceled")
            else:
                print("Account does not exist, transaction canceled")
                
            uinput=input("Enter account name, or 'Stop' to exit: ")
            
    except IOError:
        print("Input file not found, program will exit")
        
main()
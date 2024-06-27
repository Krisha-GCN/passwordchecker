#password generator

password = input("Enter a password?: ")
password = list(password)
# print(password)
    
# vars for symbol check while loop
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
i = 0
val = 7

if 8 < len(password) < 15: #check len

    # check symbols
    while val >= 7:
        if i >= len(symbols):
            print("reject")
            exit()
        elif symbols[i] in password:
            password.pop(i)
            print(password)
            val += 1
            print("accept")

        else:
            i += 1

    "".join(password) #turns password into str to do below funcs
    if password.isalnum():  #Returns True if all characters in the string are alphanumeric
        if password.isupper() and password.islower() == False: # if mix of upper & lower --> False; else one would be True
            print("Accept!")
else:
    print("Reject")

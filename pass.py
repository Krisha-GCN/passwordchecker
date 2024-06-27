#password generator

password = input("Enter a password?: ")
password = list(password)
# print(password)
    
# vars for symbol check while loop
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
i = 0
val = True

if 8 < len(password) < 15: #check len

    # check symbols
    while val:
        if i >= len(symbols):
            print("reject")
            val = False
        elif symbols[i] in password:
            print("accept")
            val = False
        else:
            i += 1

        num = 0
        something = True
        while something:
            if symbols[num] in password:
                password.pop(num)
                num += 2
            else:
                num += 1
            


        "".join(password)
        if password.isalnum():  #Returns True if all characters in the string are alphanumeric
            if password.isupper() and password.islower() == False: # if mix of upper & lower --> False; else one would be True
                print("Accept!")
else:
    print("Reject")

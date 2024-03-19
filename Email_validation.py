email=input("Enter your email address :")
if len(email)>=15:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                print("correct email ")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")

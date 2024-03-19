email=input("Enter your email address :")
if len(email)>=15:
    if email[0].isalpha() and email[0]!=email.isdigit():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                if email.count(".")<=1:
                    for i in email:
                        if i!=i.isspace():
                            pass
                        if i=="_" or i=="." or i=="@":
                            print("Correct Email ")
                            break
                    else:
                        print("Wrong email 6")

                else:
                    print("Wrong email 5")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
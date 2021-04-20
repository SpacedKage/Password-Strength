import re


print ("Enter a password\n\nThe password must be between 6 and 12 characters.\n")
def password():


    while True:
        password = input("Password: ...")
    if len(password) < 6 or len(password) > 12:
         
        print ("The password must be betwen 6 and 12 characters.\n")

password_scores = {0:"Nah,cmon", 1:"Weak", 2:"Okay,but could do better", 3: "Solid"}
password_strength = dict.fromkeys(["has_upper", "has_lower", "has_num"], False)

if re.search(r"[A-Z]", password):
        password_strength["has_upper"] = True
if re.search(r"[a-z]", password):
        password_strength["has_lower"] = True
if re.search(r"[0-9]", password):
        password_strength["has_num"] = True

score = len([b for b in password_strength.values() if b]) 

print ("Password is %s" % password_scores[score])
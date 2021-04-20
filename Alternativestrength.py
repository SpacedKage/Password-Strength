import re
 
print("Enter a password\n\nThe password must be between 6 and 12 characters.\n")
password_input = input("Password: ...")
 
 
def password_strength_check(password):
    print(f"hello the password entered is {password}")
 
    while True:
        password = input("Password: ...")
        if len(password) < 6 or len(password) > 12:
            password_scores = {0:"Nah,cmon", 1:"Weak", 2:"Okay,but could do better", 3: "Solid"}
            password_strength = dict.fromkeys(["has_upper", "has_lower", "has_num"], False)
    if re.search(r"[A-Z]", password):
        password_strength["has_upper"] = True
    if re.search(r"[a-z]", password):
        password_strength["has_lower"] = True
    if re.search(r"[0-9]", password):
        password_strength["has_num"] = True
 
test = password_strength_check(password)
 
print(test)
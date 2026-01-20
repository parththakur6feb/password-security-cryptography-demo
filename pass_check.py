'''
CONSTRAINTS :

Length ≥ 8

Contains:

at least 1 uppercase letter

at least 1 lowercase letter

at least 1 digit

at least 1 special character '''


import hashlib


while True:
    upper = False
    lower = False
    digit = False
    sp_char = False
    pass_check = True

    password = str(input("enter password: "))
    if len(password) < 8:
        print("enter password of length greater than 8")
        continue
    elif len(password) > 20:
        print("enter password of length less than 20")
        continue

    for p in password:
        if p.isupper():
            upper = True
        elif p.islower():
            lower = True 
        elif p.isdigit():
            digit = True
        elif not p.isalnum():
            sp_char = True

    # print(f"upper = {upper},lower = {lower},digit = {digit},special charachter = {sp_char}")

    if not upper:
        print("missing uppercase")
        pass_check = False
    if not lower:
        print("missing lowercase")
        pass_check = False
    if not digit:
        print("missing digit")
        pass_check = False
    if not sp_char:
        print("missing special character")
        pass_check = False
    if pass_check:
        break

hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("SHA-256 Hash:", hashed_password)





import base64
print ("......Encoding......")

ac_name = input("Enter ac_name : ")
user_name =  input("Enter User_name of account :")
password = input("Enter password : ")
encobyt = base64.b64encode(password.encode("utf-8"))
password_enc = str(encobyt, "utf-8")

print(ac_name)
print(user_name)
print (password_enc)

print ("......De-coding......")
ac_name = input("Enter ac_name : ")
passwordd = password_enc ;
decobyt = base64.b64decode(passwordd)
password_decode = str(decobyt , "utf-8")

print ("your password is : ")
print (password_decode)
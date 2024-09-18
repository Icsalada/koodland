import random
caracteres="+-_/*!&$#?=abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length=int(input("Escriba la longitud de su contraseña"))
password=""
for i in range(pass_length):
    password +=random.choice(caracteres)
print(password)

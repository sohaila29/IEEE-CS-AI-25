def password_generator():
    numbers = "0123456789"
    lowercse = "abcdefghijklmnopqrstuvwxyz"
    uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    

    all = numbers+ lowercse+ uppercase
    password = ""
    for i in range(8):
        p = (i * 4 + 5) % len(all)
        password += all[p]

    return password

print("Generated Password: ", password_generator())
      
"""
import random

daf password_generator():
    numbers = "0123456789"
    lowercse = "abcdefghijklmnopqrstuvwxyz"
    uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all = numbers+ lowercse+ uppercase
    password = ""
    for i in range(8):
        password += random.choice(all)
    return password
print("Generated Password: ", password_generator())
"""
import random
import string
charVal=string.ascii_letters + string.digits +string.punctuation

password=""
for i in range(1,9):
    password+=random.choice(charVal)

print(password)    
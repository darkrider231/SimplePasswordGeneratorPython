# From: https://www.pythonforbeginners.com/code-snippets-source-code/script-password-generator
import string 
from random import *

characters = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(characters) for x in range(randint(8, 16)))
s = "Simple Password Generator: "

print(s)
print(password)
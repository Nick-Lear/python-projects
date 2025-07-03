import string
import random
import secrets


def random_length(): #Function to randomly select length of generated password
    length = random.randint(8, 30)
    return length

pass_length = random_length() #Using random_length function to get password length
print(f"random length is: {pass_length}") #Prints above value for validation

#Print random characters from alphabet for length pass_length
def generator():
    gen_password = ""  # Creating empty variable
    # Creating a list of characters with upper/lower case letters, numbers, symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    i=0
    while i < pass_length:
        # appends output of randomly selected characters to password
        gen_password += (secrets.choice(alphabet))
        i += 1
    return gen_password

#Stores generated password into output
password = generator()

print(password)
import string
import random
import secrets


try: #Basic error handling of bad inputs -- best I can do for now
    #Gathering min/max password length from user
    min_password = int(input("Enter minimum desired password length: "))
    max_password = int(input("Enter maximum desired password length: "))
except ValueError:
    print("Please enter a valid value.")
    exit()

def random_length(min_length, max_length): #Function to randomly select length of generated password
    length = random.randint(min_length, max_length)
    return length

pass_length = random_length(min_password, max_password) #Using random_length function to get password length
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
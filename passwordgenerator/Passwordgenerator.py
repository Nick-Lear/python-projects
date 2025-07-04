import string
import random
import secrets

def random_length(min_length, max_length): #Function to randomly select length of generated password
    length = random.randint(min_length, max_length)
    return length

#Print random characters from alphabet for length pass_length
def generator():
    # Creating a list of characters with upper/lower case letters, numbers, symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        gen_password = ""
        # appends output of randomly selected characters to password
        for char in range(pass_length):
            gen_password += (secrets.choice(alphabet))
        #Checks generated password for duplicates UNTIL dupe_check is FALSE
        if not dupe_check(list(gen_password)):
            print("Password is: ")
            print(gen_password)
            return gen_password
        else:
            print("Password is invalid. Generating new password...")

#Character duplication check
def dupe_check(lst):
    # For each iteration between item 2 and end of the list - 2 places
    for index in range(2, len(lst)-2):
        #Compares each iteration to 2 iterations ahead/behind it to find 3 place duplicates
        if lst[index] == lst[index - 1] == lst[index - 2] or lst[index] == lst[index + 1] == lst[index + 2]:
            print("Password has 3 serial duplicates")
            return True
    return False


try: #Basic error handling of bad inputs -- best I can do for now
    #Gathering min/max password length from user
    min_password = int(input("Enter minimum desired password length: "))
    max_password = int(input("Enter maximum desired password length: "))
#Checks to make sure input is Int
except ValueError:
    print("Please enter a valid value.")
    exit()

#Using random_length function to get password length
pass_length = random_length(min_password, max_password)
#Prints above value for validation
#print(f"random length is: {pass_length}")
generator()
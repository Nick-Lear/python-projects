import string
import random
import secrets

def random_length(min_length, max_length):
    #Randomly select length of generated password, min < length < max
    length = random.randint(min_length, max_length)
    return length

#Print random characters from alphabet for length pass_length
def generator():
    # Creating a list of characters with upper/lower case letters, numbers, symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        gen_password = ""
        #Appends output of randomly selected characters to generate password
        for char in range(pass_length):
            gen_password += (secrets.choice(alphabet))

        pass_list = list(gen_password)

        if (
            #Checks that capital letter is present
            cap_check(pass_list)
            #Checks that lowercase letter is present
            and lowercase_check(pass_list)
            #Checks that number is present
            and num_check(pass_list)
            #Checks that symbol is present
            and sym_check(pass_list)
            #Checks for duplicates, dupe_check is FALSE when no dupes
            and dupe_check(pass_list)
        ):
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
            return False
    return True

#Checks for capital letter
def cap_check(lst):
    alphabet_cap = list(string.ascii_uppercase)
    if any(char in alphabet_cap for char in lst):
        return True
    else:
        return False


#Checks for lowercase letter
def lowercase_check(lst):
    alphabet_lower = list(string.ascii_lowercase)
    if any(char in alphabet_lower for char in lst):
        return True
    else:
        return False

#Checks for number
def num_check(lst):
    alphabet_num = list(string.digits)
    if any(char in alphabet_num for char in lst):
        return True
    else:
        return False

#Checks for symbol
def sym_check(lst):
    alphabet_sym = list(string.punctuation)
    if any(char in alphabet_sym for char in lst):
        return True
    else:
        return False

try:
    #Gathering min/max password length from user
    min_password = int(input("Enter minimum desired password length: "))
    max_password = int(input("Enter maximum desired password length: "))
#Checks to make sure input is Int
except ValueError:
    print("Please enter a valid value.")
    exit()

#Using random_length function to get password length
pass_length = random_length(min_password, max_password)
generator()
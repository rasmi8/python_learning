import random

alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]


numbers = ['0','1','2','3','4','5','6','7','8','9']

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '_', '+', '-', '=', '{', '}',
    '[', ']', '|', '\\', ':', ';', '"', "'",
    '<', '>', ',', '.', '?', '/'
]

all_characters = alphabets + numbers + special_characters
print(all_characters)

while True:
            
        try:
            pass_length = int(input("Enter password length you desire to generate: "))
            
            password = ""
                
            for i in range(pass_length):
                char = random.choice(all_characters)
                password = password + char
            print("Your generated password is : ", password)
            break
            
        except NameError:
            print("Enter a number not a character : \n")
        except ValueError:
            print("Enter a number not a character : \n")            
#0 - Data
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

SEPARATOR = "=" * 35
LOGGINS = {'bob' : '123',
           'ann' : 'pass123',
           'mike' : 'password123',
           'liz' : 'pass123'}

#1 - Welcome user
print(SEPARATOR)
print('Hello user! WAZZUP?')
print(SEPARATOR)

#2 - Ask for username and password
user = input('Please enter your username: ')
pw = input('Please enter your password: ')

#3 - Check username + password
if user not in LOGGINS.keys():  #check user
    print('INCORRECT USERNAME. TERMINATING')
    exit()

if LOGGINS.get(user) != pw: #check user+pw
    print('INCORRECT PASSWORD. TERMINATING')
    exit()
else:
    print(SEPARATOR)
    print(f'Welcome user {user}')

#4 - User chooses text
texts_index = list(range(1, len(TEXTS) + 1))
text_choice = int(input(f'Please choose text index out of {texts_index}: '))

if text_choice not in texts_index:  #check valid text choice
    print('INCORRECT CHOICE. TERMINATING')
    exit()

#5 - Text statistics
text_split =  TEXTS[text_choice - 1].split()

n_of_words = len(text_split)

n_of_titlecase = 0
n_of_uppercase = 0
n_of_lowercase = 0
n_of_numbers = 0
sum_of_numbers = 0  #for task 7
for word in text_split:
    if word.istitle():
        n_of_titlecase += 1
    elif word.isupper():
        n_of_uppercase += 1
    elif word.islower():
        n_of_lowercase += 1
    elif word.isdigit():
        n_of_numbers += 1
        sum_of_numbers += int(word) #for task 7

print(SEPARATOR)
print(f"There are {n_of_words} words.")
print(f"There are {n_of_titlecase} titlecase words.")
print(f"There are {n_of_uppercase} uppercase words.")
print(f"There are {n_of_lowercase} lowercase words.")
print(f"There are {n_of_numbers} numbers.")
print(SEPARATOR)

#6 Graphical interpretation
graph_input = dict()
char_to_replace = ".,!?"

for word in text_split:
    for char in char_to_replace:    #get rid of punctuation
        word = word.replace(char,"")
    if len(word) in graph_input.keys(): #adds to already created key
        graph_input[len(word)] += 1
    else:   #creates missing key
        graph_input[len(word)] = 1

for row in sorted(graph_input): #print graph
    print(f"{row} {'*' * graph_input[row]} {graph_input[row]}")

#7 Sum of numbers in text
print(SEPARATOR)
print(f'If we summed all the numbers in text we would get: {sum_of_numbers}')
print(SEPARATOR)
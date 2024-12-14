"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Jochcová (Kerberová)
email: michaela.kerberova@gmail.com
discord: k.michaela
"""

import sys

# valid user credentials
registered_users = {
"bob": "123",
"ann": "pass123",
"mike": "password123",
"liz": "pass123"
}

# user fills login name and password
username = input("username: ")
password = input("password: ")

separator = "-" * 40
print(separator)

# credentials check
if username in registered_users and password == registered_users[username]:
    print(f"Welcome to the app, {username}", "We have 3 texts to analyze.", sep="\n")
else:
    print("unregistered user, terminating the program.")
    sys.exit()
    
print(separator)

# texts to analysis
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

# user fills text number
while True:
    try:
        user_input = int(input("Enter a number btw. 1 and 3 to select: "))
        if user_input in range(1, 4):
            break
        else:
            print("Try again.")
    except ValueError:
        print("Try again.")

print(separator)

# text analysis
analyzed_text = TEXTS[(user_input) - 1]

cleaned_text = list()
titlecase_words = list()
uppercase_words = list()
lowercase_words = list()
numbers = list()
word_lenght_all = dict()

for word in analyzed_text.split():
    cleaned_text.append(word.strip(".,:;"))

word_count = len(cleaned_text)

for word in cleaned_text:
    if word.istitle() and word.isalpha():
        titlecase_words.append(word)
    elif word.isupper() and word.isalpha():
        uppercase_words.append(word)
    elif word.islower() and word.isalpha():
        lowercase_words.append(word)
    elif word.isnumeric():
        numbers.append(word)
    word_lenght = len(word)
    word_lenght_all[word_lenght] = word_lenght_all.get(word_lenght, 0) + 1

titlecase_words.extend(uppercase_words)

titlecase_word_count = len(titlecase_words)
uppercase_word_count = len(uppercase_words)
lowercase_word_count = len(lowercase_words)
numbers_count = len(numbers)
numbers_sum = sum(int(number) for number in numbers)

print(f"""
There are {word_count} words in the selected text.
There are {titlecase_word_count} titlecase words.
There are {uppercase_word_count} uppercase words.
There are {lowercase_word_count} lowercase words.
There are {numbers_count} numeric strings.
The sum of all the numbers is: {numbers_sum}.
"""
)

print(separator)

# bar chart
occurence_column_width = max(word_lenght_all.values())

print(f"{'LEN': >4} | {'OCCURENCE': ^{occurence_column_width}} | NR.")
print(separator)
for lenght, count in sorted(word_lenght_all.items()):
    print(f"{lenght: >4} | {('*' * count): <{occurence_column_width}} | {count}")
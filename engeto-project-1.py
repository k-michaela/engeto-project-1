"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Jochcová (Kerberová)
email: michaela.kerberova@gmail.com
discord: k.michaela
"""

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
    print("unregistered user, terminating the program..")

print(separator)

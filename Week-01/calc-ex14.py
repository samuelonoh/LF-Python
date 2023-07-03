from sys import argv
script, username = argv
hello_are_you_there = '--> '

print(f"This is {script} script file")
print(f"Answer these few questions {username}")

print(f"{username}, how old are you?")
age = input(hello_are_you_there)

print(f"where do you hail from {username}?")
background = input(hello_are_you_there)

print(f"""
    My name is {username}.
    I am {age} years old.
    I hail from {background}
    """)
# Ask user for their name,
# remove whitespace from str
# capitalize user's name
# split user's name into first name and last name
[first, last] = input("What's your name? ").strip().title().split(" ")

value: str = 12.34

print(f"type: {type(value)} value: {value}")

# Say hello to user
print(f"hello, {first}, {last}")

value1 = (int)(input("Insert 1st value "))

value2 = (int)(input("Insert 2nd value "))

print(f"{value1 + value2}")
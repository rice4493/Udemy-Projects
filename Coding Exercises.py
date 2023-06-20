# day 1 Coding Exercise 1

prompt = "What is your name? "
name = (input(prompt))
print(type(name))

# day 1 Coding Exercise 2

age = input("How old are you? ")
print(age)

# day 1 Coding Exercise 3

fruits = ['apple', 'banana', 'mango', 'orange']

# day 3 coding exercise1

while True:
    country = input("Which country do you come from?")
    match country:
        case 'USA':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'Germany':
            print("Hallo")
        case '_':
            print("Oops! unknown country :(")

# day 3 coding exercise2

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for item in ingredients:
    item = item.title()
    print(item)

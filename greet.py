def greet(name):
    now = datetime.datetime.now()
    return f"Hello, {name}! The current date and time is {now:%Y-%m-%d %H:%M:%S}."
    return f"Hello, {name}! Welcome to GitHub."

if __name__ == "__main__":
    user = input("Enter your name:")
    print(greet(user))

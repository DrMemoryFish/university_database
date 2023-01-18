def tell_joke():
    try:
        favorite_number = int(input("Pick a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number between 1 and 100.")
        return

    if favorite_number < 10:
        print("Why was the math book sad? It had too many problems.")
    elif 10 <= favorite_number < 50:
        print("Why was the computer cold? It left its Windows open.")
    elif 50 <= favorite_number <= 100:
        print("Why couldn't the bicycle stand up by itself? It was two-tired.")
    else:
        print("Please enter a valid number between 1 and 100.")
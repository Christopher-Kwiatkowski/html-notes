def order():
    food = input(
        "Please place your order. Would you like waffles or pancakes?\n").lower()
    for index in range(len(food)):
        if food[index:index+7] == "waffles":
            return print(f"{food[index:index+7]} it is!")
        elif food[index:index+8] == "pancakes":
            return print(f"{food[index:index+8]} it is!")
    print("I dont understand")
    order()


order()

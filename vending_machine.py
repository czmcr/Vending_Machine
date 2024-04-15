def vending_machine(choice, money_insert):

    #drinks database
    items = ["Coca-Cola", "Pepsi", "100 Plus"]
    prices = [53, 15, 3]
    price = prices[items.index(choice)]

    #verify input
    if choice not in items:
        return "Invalid. Please select a valid drink."

    #check eror
    if money_insert < price:
        return f"Insufficient amount. Please insert at least RM{price}."
    
    change = money_insert - price
    money__return = calculate_change(change)

    response = f"You bought a {choice} for RM{price}."
    if change > 0:
        response = f"Your change is RM{change}: {money__return}"
    else:
        response = "No change. Thank you!"

    return response

def calculate_change(change):
    exchange_notes = [100, 50, 20, 10, 5, 1] 
    result = {}

    for note in exchange_notes:
        if change >= note:
            count = change // note
            result[f"RM{note}"] = count
            change %= note

    return result


#test case
print('''
    Drinks         Price(RM)
    -----------------------
    Coca-Cola       53
    Pepsi           15
    100 Plus         3
''')
user_input = input("Please select a drink (Coca-Cola, Pepsi, 100 Plus): ")
money_insert = int(input("Please insert money (RM): "))

output = vending_machine(user_input, money_insert)
print(output)

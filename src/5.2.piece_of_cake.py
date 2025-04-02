def get_recipe_price(prices, optionals=None, **kwargs):
    """
    calc the total cost on the recipe
    """
    # price is for 100 grams.. 
    # if no amout was given then get one unit (100grams)
    if optionals is None:
        optionals = []
    total = 0
    for ing, amount in kwargs.items():
        if ing in prices and ing not in optionals:
            # price is for 100 grams
            total += (amount / 100) * prices[ing]
    print(total)


def test():
    get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
    get_recipe_price({})

if __name__=="__main__":
    test()
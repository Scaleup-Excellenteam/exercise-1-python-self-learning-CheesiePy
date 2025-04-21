def piece_of_cake(prices, optionals=None, **kwargs):
    """
    calc the total cost on the recipe
    Args:
    - prices (dict): A dictionary containing the prices of ingredients.
    - optionals (list): A list of optional ingredients.
    - **kwargs: Keyword arguments representing the ingredients and their amounts.
    Returns:
    - dict: A dictionary containing the total cost of the recipe.
    """
    # price is for 100 grams.. 
    # if no amout was given then get one unit (100grams)
    if optionals is None:
        optionals = []
    
    return sum((amount / 100) * prices[ing] for ing, amount in kwargs.items() if ing in prices and ing not in optionals)



def test():
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({}))

if __name__=="__main__":
    test()
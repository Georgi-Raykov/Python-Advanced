def shop_from_grocery_list(budget, products, *args):
    bought_products = []

    for items in args:

        product = items[0]
        price = float(items[1])

        if budget > price and product not in bought_products and product in products:
            bought_products.append(product)
            budget -= price
        else:
            break
    result = ''
    missing_products = [x for x in products if x not in bought_products]
    if len(bought_products) == len(products):
        result += f"Shopping is successful. Remaining budget: {budget:.2f}"
    else:
        result += f"You did not buy all the the products. Missing products: {', '.join(missing_products)}."
    return result


print(shop_from_grocery_list(100, ['tomato', 'cola'], ('cola', 5.8), ('tomato', 10.0), ('tomato', 20.45)))
print()
print(shop_from_grocery_list(100, ['tomato', 'cola', 'chips', 'meat'], ('cola', 5.8), ('tomato', 10.0), ('meat', 22)))
print()
print(shop_from_grocery_list(100, ['tomato', 'cola', 'chips', 'meat', 'chocolate'],
                             ('cola', 15.8), ('chocolate', 30), ('tomato', 15.85), ('chips', 50), ('meat', 22.99)))
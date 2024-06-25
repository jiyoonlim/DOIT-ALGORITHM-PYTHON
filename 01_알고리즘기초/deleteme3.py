original_price = float(input('Original price $: '))
discount_rate = float(input('Discount rate %: '))

discount_price = original_price * (1-(discount_rate/100))

print(f'Final price is $ {discount_price}')
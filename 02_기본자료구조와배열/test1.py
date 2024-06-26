quantity = int(input("Enter the quantity you want to purchase: "))

def price(q):
  if q < 10:
    total_price = q * 100
  elif q < 30:
    total_price = q * 95
  elif q < 100:
    total_price = q * 90
  else:
    total_price = q * 85

  return total_price


print(price(quantity))
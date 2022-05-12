prices=[69,158,188,277,355,467]
def inc_price(price):
    return price+10
new_prices=list(map(inc_price,prices))
print(new_prices)

new_prices=list(map(lambda x: x+10, prices))
print(new_prices)
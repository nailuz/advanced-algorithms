coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
def core(value):
    the_change = []
    number_coins = 0
    for row in coins:
        value = round(value, 2)
        the_change.append({row: value//row})
        number_coins += value//row
        value -= row*(value//row)
    return the_change, number_coins

print(core(4.35))

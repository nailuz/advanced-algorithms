def multiplier(first_value, secound_value):
    if secound_value == 1:
        return first_value
    else:
        return first_value + multiplier(first_value, secound_value -1)

def exponential(first_value, secound_value):
    if secound_value == 1:
        return first_value
    else:
        return first_value * exponential(first_value, secound_value -1)

def pluser(value):
    if value == 0:
        return 0
    else:
        return value + pluser(value-1)
    
def fibonacci(anterior, atual):
    if atual > 9999999:
        return str(atual)
    else:
        proximo = anterior + atual
        return str(atual)+' '+(fibonacci(atual, proximo))

print(multiplier(5,5))
print(exponential(2,11))
print(pluser(5))
print(fibonacci(0,1))

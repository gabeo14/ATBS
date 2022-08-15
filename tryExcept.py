def divide42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('You tried to divide by zero.')

        
print(divide42by(4))
print(divide42by(6))
print(divide42by(0))
print(divide42by(3))
def string(text):
    invert= text[::-1]
    return invert

text = input('Digite un texto: ')
print(f"El texto invertido es: {string(text)}")

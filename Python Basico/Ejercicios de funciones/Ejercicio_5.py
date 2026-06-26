def count_letters(string):
    uppercase = 0
    lowercase = 0
    for letter in string:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
    print(f"La cantidad de letras mayúsculas es: {uppercase} y la cantidad de letras minúsculas es: {lowercase}")
    

count_letters("Hello World!")

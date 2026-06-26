import csv #importa el módulo csv para leer archivos csv


def read_list_games(file_path):# define la función read_list_games que toma como argumento el file_path (ruta del archivo csv)
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file) # DirectReader lee el archivo csv y lo convierte en un diccionario, donde cada fila es un diccionario con las claves correspondientes a los encabezados del archivo csv
        games = [] # con esta lista vacia, se creara una lista de diccionarios con los datos de cada juego
        for row in reader:
            games.append(row)
    return games


def amount_games_for_genre(games):# define la función amount_games_for_genre que toma como argumento la lista de juegos (games) y devuelve un diccionario con la cantidad de juegos por género
    genres = {} # se crea un diccionario vacío para almacenar la cantidad de juegos por género
    for game in games: # recorremos cada juego en la lista de juegos
        genre = game['genre']
        if genre in genres: # si el género ya está en el diccionario, se incrementa su cantidad en 1
            genres[genre] += 1 # si el género no está en el diccionario, se agrega con una cantidad de 1
        else: 
            genres[genre] = 1 # se agrega el género al diccionario con una cantidad de 1
    return genres # se devuelve el diccionario con la cantidad de juegos por género


def main():
    list_games = 'list_games.csv'
    games = read_list_games(list_games)
    amounts = amount_games_for_genre(games)
    print("Géneros encontrados:")
    for genre in sorted(amounts):# se ordenan los géneros alfabéticamente y se imprime cada género junto con su cantidad de juegos
        print(f"{genre}: {amounts[genre]}")


if __name__ == "__main__":
    main()
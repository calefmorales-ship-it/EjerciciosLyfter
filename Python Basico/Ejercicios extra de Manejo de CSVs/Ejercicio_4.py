import csv

def read_list_games(file_name):# Lee el archivo CSV y devuelve una lista de diccionarios con la información de los videojuegos.
    games = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append(row)
    return games


def find_developer_games(file_name, developer_name):# Busca y muestra los videojuegos desarrollados por un desarrollador específico.
    games = read_list_games(file_name)
    print(f"\nVideojuegos desarrollados por {developer_name}:")
    for game in games:
        if game['developer'].lower() == developer_name.lower():
            print(
                f"- {game['name']} "
                f"(Rating: {game['rating']}, "
                f"Genre: {game['genre']})"
            )


def main():

    file_name = 'list_games.csv' # Nombre del archivo CSV que contiene la información de los videojuegos.
    developer_name = input("Ingrese el nombre del desarrollador: ") # Solicita al usuario que ingrese el nombre del desarrollador.
    find_developer_games(file_name,developer_name)# Llama a la función para buscar y mostrar los videojuegos desarrollados por el desarrollador ingresado por el usuario.

if __name__ == "__main__":
    main()
import csv #librería para manejar archivos CSV

def write_games(file_path, games):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
       headers = games[0].keys() #obtenemos los nombres de las columnas a partir de las claves del primer diccionario
       writer = csv.DictWriter(
           file,
           fieldnames=headers,
           delimiter='\t'
       ) #creamos un objeto DictWriter para escribir en el archivo CSV, especificando el delimitador como tabulación

       writer.writeheader() #escribimos los encabezados en el archivo CSV

       writer.writerows(games) #escribimos las filas de datos en el archivo CSV

def input_game_data():
    game_name = input("Ingrese el nombre del juego: ")
    game_genre = input("Ingrese el género del juego: ")
    game_developer = input("Ingrese el desarrollador del juego: ")
    esrb_rating = input("Ingrese la calificación ESRB: ")
    return {'nombre': game_name, 'genero': game_genre, 'desarrollador': game_developer, 'clasificacion': esrb_rating}

def main():
    games = []
    while True:
        game_data = input_game_data() #obtenemos los datos del juego a través de la función input_game_data
        games.append(game_data) #agregamos el diccionario con los datos del juego a la lista de juegos
        cont = input("¿Desea ingresar otro juego? (s/n): ")
        if cont.lower() != 's': #si el usuario no desea ingresar otro juego, salimos del bucle
            break
    write_games('games.csv', games) #escribimos los datos de los juegos en el archivo CSV

if __name__ == "__main__":
    main() #ejecutamos la función principal para iniciar el programa
import json

# Leer pokémones del archivo
def leer_pokemones():
    with open("Pokemons.json", "r") as archivo:
        pokemones = json.load(archivo)
    return pokemones


# Solicitar datos al usuario
def request_pokemon_data():
    name = input("Nombre del Pokémon: ")
    type = input("Tipo: ")
    level = int(input("Nivel: "))
    weight_kg = float(input("Peso en kg: "))
    return name, type, level, weight_kg


# Crear nuevo pokémon
def create_new_pokemon(name, type, level, weight_kg):
    return {
        "name": name,
        "type": type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": False,
        "held_item": None,
        "skills": [],
        "stats": {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "sp_attack": 0,
            "sp_defense": 0,
            "speed": 0
        }
    }


# Agregar a la lista
def add_pokemon(pokemones, new_pokemon):
    pokemones.append(new_pokemon)


# Guardar archivo
def save_pokemones(pokemones):
    with open("Pokemons.json", "w") as archivo:
        json.dump(pokemones, archivo, indent=4)


def main():
    pokemones = leer_pokemones()
    name, type, level, weight_kg = request_pokemon_data()
    new_pokemon = create_new_pokemon(name,type, level,weight_kg)
    add_pokemon(pokemones, new_pokemon)
    save_pokemones(pokemones)
    print("Pokémon agregado correctamente.")
    print()
    print(pokemones)


if __name__ == "__main__":
    main()
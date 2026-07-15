import json

# Leer los pokémon  del archivo JSON
with open("Pokemons.json", "r") as archivo:
    pokemones = json.load(archivo) # convierte el JSON a una lista de diccionarios

# Pedir datos del nuevo pokémon. Solo se piden los datos básicos, el resto se asigna por defecto ya que desconozco sobre el pokémon que se va a agregar. En un caso real, se podrían pedir más datos o asignar valores específicos según el tipo de pokémon.
name = input("Nombre del Pokémon: ")
type = input("Tipo: ")
level = int(input("Nivel: "))
weight_kg = float(input("Peso en kg: "))

# Crear el nuevo pokémon
nuevo_pokemon = {
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
pokemones.append(nuevo_pokemon)

# Guardar en el archivo
with open("Pokemons.json", "w") as archivo:
    json.dump(pokemones, archivo, indent=4)

print("Pokémon agregado correctamente.")
print('')
print(pokemones)
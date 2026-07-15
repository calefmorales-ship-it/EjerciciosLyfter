def ordered_words(string_words):
    words_list = string_words.split("-") # El split convierte la cadena de texto en una lista de palabras, utilizando el guion como separador
    ordered_words = sorted(words_list) # La función sorted ordena la lista de palabras alfabéticamente y devuelve una nueva lista con las palabras ordenadas. La lista original no se modifica.
    new_string_words = "-".join(ordered_words) # El join convierte la lista de palabras ordenadas en una cadena de texto, utilizando el guion como separador
    return new_string_words # se devuelve la cadena de texto con las palabras ordenadas alfabéticamente


def main():
    string_words = 'casa-zorro-raton-funcion-ejercicio-ordenar-barco-hielo'
    ordered_string_words = ordered_words(string_words)
    print("Cadena original: ", string_words)
    print("Cadena ordenada: ", ordered_string_words)
main()
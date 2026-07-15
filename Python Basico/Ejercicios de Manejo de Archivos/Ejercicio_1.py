def read_songs_by_lines(songs): #función para leer canciones por líneas
    my_songs = []               #inicializar lista para almacenar las canciones
    with open(songs, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines: #recorrer cada línea del archivo y agregarla a la lista de canciones
            my_songs.append(line.strip())
    my_songs.sort() #ordenar la lista de canciones alfabéticamente
    
    # Crear nuevo archivo
    with open('songs_ordered.txt', 'w', encoding='utf-8') as new_file:
            for song in my_songs: #recorrer la lista de canciones ordenadas y escribir cada canción en el nuevo archivo
                new_file.write(song + "\n")

    # escribir las canciones ordenadas en el nuevo archivo
    with open('songs_ordered.txt', 'r', encoding='utf-8') as new_file:
        print(new_file.read())


read_songs_by_lines('Songs.txt')

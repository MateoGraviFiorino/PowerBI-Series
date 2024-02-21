import requests
import os

# Configura tu clave de API de TMDb
API_KEY = 'dc9e8e54e9c0d870659fb83b17bba1c2'

def descargar_poster_tmdb(nombre_serie):
    # Realiza una consulta a la API de TMDb para buscar la serie por su nombre
    url_busqueda = f'https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&query={nombre_serie}'
    respuesta_busqueda = requests.get(url_busqueda)
    datos_serie = respuesta_busqueda.json()

    # Verifica si se encontraron resultados de la búsqueda
    if datos_serie['total_results'] > 0:
        # Obtiene el ID de la serie (selecciona el primer resultado)
        id_serie = datos_serie['results'][0]['id']

        # Realiza una consulta para obtener los detalles de la serie, incluyendo los pósters
        url_detalles = f'https://api.themoviedb.org/3/tv/{id_serie}?api_key={API_KEY}'
        respuesta_detalles = requests.get(url_detalles)
        detalles_serie = respuesta_detalles.json()

        # Descarga los pósters de la serie
        ruta_carpeta_posters = 'C:\Users\mateo\OneDrive\Escritorio\SERIES\Posters'
        os.makedirs(ruta_carpeta_posters, exist_ok=True)

        for poster in detalles_serie['posters']:
            url_poster = f"https://image.tmdb.org/t/p/original{poster['file_path']}"
            nombre_archivo = f"{id_serie}_{poster['file_path'].split('/')[-1]}"
            ruta_archivo = os.path.join(ruta_carpeta_posters, nombre_archivo)
            with open(ruta_archivo, 'wb') as archivo:
                respuesta_imagen = requests.get(url_poster)
                archivo.write(respuesta_imagen.content)
            print(f"Poster descargado: {ruta_archivo}")
    else:
        print("No se encontraron resultados para la serie.")

# Ejemplo de uso
nombre_serie = input("100 Humans")
descargar_poster_tmdb(nombre_serie)

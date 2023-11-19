import requests
from bs4 import BeautifulSoup

# Lista de URLs que deseas scrapear
urls = [
    'https://www.ejemplo.com/pagina1',
    'https://www.ejemplo.com/pagina2',
    'https://www.ejemplo.com/pagina3',
    # Agrega más URLs según sea necesario
]

# Crear un archivo para guardar los resultados
with open('resultados.txt', 'w', encoding='utf-8') as file:
    # Iterar sobre las URLs
    for url in urls:
        # Realizar la solicitud HTTP a la página
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontrar todos los enlaces en la página
            links = soup.find_all('a')

            # Iterar sobre los enlaces y guardar el texto y la URL en el archivo
            for link in links:
                link_text = link.get_text(strip=True)
                link_url = link.get('href')
                file.write(f'Texto: {link_text}, URL: {link_url}\n')

            print(f'Scraping completado para {url}')
        else:
            print(f'Error al obtener la página {url}. Código de estado: {response.status_code}')

print('Scraping completado. Los resultados se han guardado en resultados.txt.')

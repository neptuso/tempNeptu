import requests
from bs4 import BeautifulSoup
import urllib3

# Desactivar advertencias de solicitudes HTTPS no verificadas
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def obtener_datos_meteorologicos(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
  # Buscar la tabla de condiciones actuales
    tabla = soup.find('div', class_='card').find('table', class_='tablespacer')
    
    # Extraer los datos de la tabla
    filas = tabla.find_all('tr')
    datos = {}
    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) == 2:
            etiqueta = celdas[0].text.strip()
            valor = celdas[1].text.strip()
            datos[etiqueta] = valor
    
    return datos

# Ejemplo de uso
url = 'https://urlejemplo.com'
datos = obtener_datos_meteorologicos(url)
print(datos)
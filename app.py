import os
import requests
import json

# URL del servidor HAPI FHIR
hapi_fhir_url = "http://localhost:8080/fhir"

# Ruta de la carpeta que contiene los archivos JSON
folder_path = "/ruta/a/tu/archivo.json"

# Configurar los headers
headers = {
    "Content-Type": "application/fhir+json"
}

# Autenticación básica (si es necesaria)
auth = ('', '')  # Reemplaza con tu usuario y contraseña

# Recorrer todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Verificar que sea un archivo JSON
    if os.path.isfile(file_path) and filename.endswith('.json'):
        try:
            # Leer los datos del archivo JSON
            with open(file_path, 'r') as file:
                patient_data_json = file.read()

            # Hacer la solicitud POST
            response = requests.post(f"{hapi_fhir_url}/Patient", data=patient_data_json, headers=headers, auth=auth)

            # Verificar el resultado
            if response.status_code == 201:
                print(f"Datos del archivo {filename} ingresados exitosamente")
            else:
                print(f"Error al ingresar datos del archivo {filename}: {response.status_code}")
                print(response.text)

        except FileNotFoundError:
            print(f"Archivo no encontrado: {file_path}")
        except PermissionError:
            print(f"Permiso denegado al intentar leer el archivo: {file_path}")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON: {file_path}")
        except requests.RequestException as e:
            print(f"Error en la solicitud para el archivo {filename}: {e}")

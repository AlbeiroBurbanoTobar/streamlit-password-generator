import streamlit as st
import random
import string

# Título de la app
st.title('Generador de contraseñas')
st.write('Creado por Albeiro Burbano')

# Solicitar la longitud de la contraseña
longitud = st.number_input('¿Cuál será la longitud de la contraseña?', min_value=1, value=8, step=1)

# Opciones de personalización
incluye_numeros = st.checkbox('Incluir números')
incluye_simbolos = st.checkbox('Incluir símbolos')

# Generar la contraseña
caracteres = string.ascii_letters
if incluye_numeros:
    caracteres += string.digits
if incluye_simbolos:
    caracteres += string.punctuation

contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

# Mostrar la contraseña en un campo de texto
st.write('Contraseña generada:')
st.text_area('Haga clic en el texto para copiarlo al portapapeles:', contrasena, height=50, key="contrasena")



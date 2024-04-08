import streamlit as st
import random
import string

# Configurar la paleta de colores para los checkboxes
st.markdown("""
<style>
div.row-widget.stCheckbox > div{flex-direction:row-reverse;}
div.row-widget.stCheckbox > div > label{justify-content:space-between;}
div.row-widget.stCheckbox > div > label > span{text-align:right;flex:1;}
div.row-widget.stCheckbox > div > label > div{margin-left:-10px;}
</style>
""", unsafe_allow_html=True)

# Título de la app
st.markdown('## Personalice su contraseña')

# Personalización de la contraseña
longitud = st.slider('Longitud de la contraseña', min_value=1, max_value=20, value=12, step=1)

# Opciones de personalización
mayusculas = st.checkbox('Mayúsculas', value=True)
minusculas = st.checkbox('Minúsculas', value=True)
numeros = st.checkbox('Números', value=True)
simbolos = st.checkbox('Símbolos', value=True)

# Generar la contraseña
caracteres = ''
if mayusculas:
    caracteres += string.ascii_uppercase
if minusculas:
    caracteres += string.ascii_lowercase
if numeros:
    caracteres += string.digits
if simbolos:
    caracteres += string.punctuation

# Asegurar que se seleccione al menos una opción
if not caracteres:
    st.error('Por favor, seleccione al menos una opción para incluir en la contraseña.')
else:
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    # Se ha removido el primer text_area que era redundante
    # Mostrar la contraseña en un campo de texto con una key única
    st.text_area('Contraseña generada:', contrasena, height=50, key="contrasena_area")




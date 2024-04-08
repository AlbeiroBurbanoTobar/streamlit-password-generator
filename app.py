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
st.markdown('## Generador de contraseñas seguras')

# Personalización de la contraseña
longitud = st.slider('Longitud de la contraseña', min_value=1, max_value=35, value=12, step=1)

# Opciones de personalización
mayusculas = st.checkbox('Mayúsculas', value=True)
minusculas = st.checkbox('Minúsculas', value=True)
numeros = st.checkbox('Números', value=True)
simbolos = st.checkbox('Símbolos', value=True)

# Botón para generar una nueva contraseña
if st.button('Generar nueva contraseña'):
    # Re-generamos la contraseña
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
        st.text_area('Contraseña generada:', contrasena, height=50, key="contrasena_area")
else:
    # Mantener la contraseña anterior si no se presiona el botón
    # Se usa la sesión state para recordar la última contraseña generada
    if 'contrasena' not in st.session_state or not st.session_state.caracteres:
        # Generar una contraseña por primera vez
        caracteres = ''
        if mayusculas:
            caracteres += string.ascii_uppercase
        if minusculas:
            caracteres += string.ascii_lowercase
        if numeros:
            caracteres += string.digits
        if simbolos:
            caracteres += string.punctuation
        
        # Guardar los caracteres en el estado de la sesión
        st.session_state.caracteres = caracteres
        
        if caracteres:
            contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
            # Guardar la contraseña en el estado de la sesión
            st.session_state.contrasena = contrasena

    st.text_area('Contraseña generada:', st.session_state.contrasena, height=50, key="contrasena_area")

# Firma
st.markdown('---')
st.markdown('Creado por Albeiro Burbano :)')





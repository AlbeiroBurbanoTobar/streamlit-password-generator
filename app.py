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
st.title('Generador de contraseñas seguras')

# Docstring para la función generar_contrasena
def generar_contrasena(longitud, caracteres):
    """
    Genera una contraseña aleatoria con la longitud y caracteres especificados.

    Args:
        longitud (int): Longitud de la contraseña.
        caracteres (str): Cadena que contiene los caracteres permitidos para la contraseña.

    Returns:
        str: Contraseña aleatoria generada.
    """
    if not caracteres:
        raise ValueError('No se han seleccionado caracteres para la contraseña.')

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena


# Personalización de la contraseña
longitud = st.slider(
    'Longitud de la contraseña',
    min_value=1,
    max_value=35,
    value=12,
    step=1,
    help='Establece la longitud de la contraseña generada.'
)

# Opciones de personalización
mayusculas = st.checkbox('Mayúsculas', value=True, help='Incluir letras mayúsculas en la contraseña.')
minusculas = st.checkbox('Minúsculas', value=True, help='Incluir letras minúsculas en la contraseña.')
numeros = st.checkbox('Números', value=True, help='Incluir números en la contraseña.')
simbolos = st.checkbox('Símbolos', value=True, help='Incluir símbolos en la contraseña.')

# Botón para generar una nueva contraseña
if st.button('Generar contraseña'):
    try:
        # Re-generar la contraseña
        caracteres = ''
        if mayusculas:
            caracteres += string.ascii_uppercase
        if minusculas:
            caracteres += string.ascii_lowercase
        if numeros:
            caracteres += string.digits
        if simbolos:
            caracteres += string.punctuation

        # Generar contraseña
        contrasena = generar_contrasena(longitud, caracteres)

        # Mostrar la contraseña generada
        st.text_area('Contraseña generada:', contrasena, height=50, key="contrasena_area")
    except ValueError as e:
        st.error(e)

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

        # Generar contraseña
        if caracteres:
            contrasena = generar_contrasena(longitud, caracteres)

            # Guardar la contraseña en el estado de la sesión
            st.session_state.contrasena = contrasena

    # Mostrar la contraseña generada
    st.text_area('Contraseña generada:', st.session_state.contrasena, height=50, key="contrasena_area")

# Firma
st.markdown('---')
st.markdown('Creado por Albeiro Burbano :)')





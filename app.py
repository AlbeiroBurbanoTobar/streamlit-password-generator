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

# Mostrar la contraseña y el botón para copiar
st.write('Contraseña generada:')
texto_copia = st.text_input('Haga clic en la contraseña para copiarla al portapapeles:', contrasena, key="contrasena", help="Haga clic en el texto para copiar")

# JavaScript para habilitar la copia al portapapeles
st.markdown("""
    <script>
    const copyToClipboard = str => {
        const el = document.createElement('textarea');
        el.value = str;
        el.setAttribute('readonly', '');
        el.style.position = 'absolute';
        el.style.left = '-9999px';
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
    };
    const copyBtn = document.getElementById('copyButton');
    copyBtn.addEventListener('click', function() {
        copyToClipboard(document.getElementById('copyText').value);
    });
    </script>
    """, unsafe_allow_html=True)

# Botón para copiar al portapapeles
if st.button('Copiar contraseña', key="copyButton"):
    st.markdown(f'<input type="text" value="{contrasena}" id="copyText" style="position: absolute; left: -9999px;">', unsafe_allow_html=True)
    st.markdown('<button id="copyButton">Copiar</button>', unsafe_allow_html=True)
    st.success('Contraseña copiada al portapapeles')


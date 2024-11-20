import streamlit as st
import json
from TM import TuringMachine

def load_machine_config(uploaded_file):
    return json.load(uploaded_file)

st.title("Máquina de Turing - Cifrado César")
st.sidebar.header("Configuración de la Máquina")

encryption_file = st.sidebar.file_uploader("Sube el archivo de configuración para encriptar", type=["json"])
decryption_file = st.sidebar.file_uploader("Sube el archivo de configuración para desencriptar", type=["json"])

if encryption_file and decryption_file:
    encryption_config = load_machine_config(encryption_file)
    decryption_config = load_machine_config(decryption_file)

    encryption_tm = TuringMachine(**encryption_config)
    decryption_tm = TuringMachine(**decryption_config)

    st.sidebar.success("Máquinas cargadas exitosamente.")
    
    # Menú principal
    st.subheader("Selecciona una acción:")
    option = st.radio("", ["Encriptar", "Desencriptar", "Ejemplos"])
    
    if option == "Encriptar":
        st.write("## Encriptar mensaje")
        message = st.text_input("Ingresa el mensaje para encriptar (formato: k#mensaje):")
        
        if st.button("Encriptar"):
            if "#" in message and len(message.split("#")) == 2:
                encrypted_message = encryption_tm.cipher(message)
                st.success(f"Mensaje encriptado: {encrypted_message}")
            else:
                st.error("El formato del mensaje es inválido. Debe ser 'k#mensaje'.")
    
    elif option == "Desencriptar":
        st.write("## Desencriptar mensaje")
        message = st.text_input("Ingresa el mensaje para desencriptar (formato: k#mensaje):")
        
        if st.button("Desencriptar"):
            if "#" in message and len(message.split("#")) == 2:
                decrypted_message = decryption_tm.cipher(message)
                st.success(f"Mensaje desencriptado: {decrypted_message}")
            else:
                st.error("El formato del mensaje es inválido. Debe ser 'k#mensaje'.")
    
    elif option == "Ejemplos":
        st.write("## Ejemplos de encriptación y desencriptación")
        examples = [
            ("N#ALAN PONGANOS COMPLETO", "NYNA CBATNABF PBZCYRGB"),
            ("P#ESTAMOS USANDO STREAMLIT", "THIPBDH JHPCSD HIGTPBAXI")
        ]
        for original, encrypted in examples:
            st.write(f"**Original:** {original}")
            st.write(f"**Encriptado:** {encrypted}")
            st.write("---")
else:
    st.warning("Sube ambos archivos de configuración para continuar.")


import streamlit as st
import base64
from pathlib import Path

# --- FUNCIÓN AUXILIAR PARA CONVERTIR IMÁGENES A BASE64 ---
# Esto es necesario para incrustar la imagen en el HTML del link
def get_image_as_base64(file_path):
    try:
        # Lee el archivo de imagen en modo binario
        with open(file_path, "rb") as f:
            data = f.read()
        # Codifica los datos en Base64
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        # Devuelve None si no se encuentra el archivo
        st.error(f"Error: No se pudo encontrar la imagen en la ruta: {file_path}")
        return None
    except Exception as e:
        st.error(f"Error al cargar la imagen {file_path}: {e}")
        return None

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
# Usamos el layout "wide" para aprovechar mejor el espacio
st.set_page_config(
    page_title="Datainsights Colombia",
    page_icon="logo_datai.png", # El ícono que aparece en la pestaña del navegador
    layout="wide"
)

# --- 8. SIDEBAR ---
with st.sidebar:
    # 8.1. Título
    st.title("DataInsights Colombia")
    
    # 8.2. Foto 1 y Nombre
    st.image("foto1.png", width=150)
    st.markdown("**Oscar Javier Carabali Portela**")
    st.caption("CEO & Co-Fundador") 
    
    st.divider() # Separador
    
    # 8.3. Foto 2 y Nombre
    st.image("foto2.png", width=150)
    st.markdown("**John Alexander Zapata Ortiz**")
    st.caption("CTO & Co-Fundador") 
    
    st.divider() # Separador
    
    # 8.4. Derechos reservados
    st.caption("© Datainsights Colombia 2025. \nTodos los derechos reservados.")

# --- PRE-CARGAR IMÁGENES COMO BASE64 ---
# Usamos los nombres de archivo que me diste (BI.png, IA.png, etc.)
img_bi_b64 = get_image_as_base64("BI.png")
img_ia_b64 = get_image_as_base64("IA.png")
img_urbox_b64 = get_image_as_base64("urbox.png")
img_iana_b64 = get_image_as_base64("IANA.png")


# --- CUERPO PRINCIPAL DE LA PÁGINA ---

# --- 1. LOGO EN CABECERA CENTRADO ---
col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image("logo_datai.png", use_column_width=True)

# --- 2. NOMBRE GRANDE EN NEGRITA (CENTRADO) ---
st.markdown("<h1 style='text-align: center; font-weight: bold;'>Datainsights Colombia</h1>", unsafe_allow_html=True)

# --- 3. INFORMACIÓN BÁSICA (CENTRADA) ---
st.markdown(
    """
    <div style='text-align: center; font-size: 1.1em;'>
    Somos una compañía especializada en analítica de datos, inteligencia de negocios e inteligencia artificial. 
    Nuestra misión es transformar los datos de nuestros clientes en decisiones estratégicas que impulsen su crecimiento.
    </div>
    """, 
    unsafe_allow_html=True
)

st.divider() # Un separador visual

# --- 4. SUBTÍTULO "QUÉ HACEMOS" ---
st.subheader("Que hacemos", divider="blue")

# --- 5. CUADROS "QUÉ HACEMOS" (B.I. y I.A.) ---
col_bi, col_ia = st.columns(2, gap="large") 

# 5.1. Cuadro 1: Business Intelligence (con imagen clickable)
with col_bi:
    with st.container(border=True):
        if img_bi_b64:
            # Usamos la URL que tenías (aún es la de ejemplo)
            st.markdown(
                f"""
                <a href='https://url-para-bi.com' target='_blank'>
                    <img src='data:image/png;base64,{img_bi_b64}' width='250' style='display: block; margin-left: auto; margin-right: auto;'>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            # Mensaje de error si no se encuentra la imagen "BI.png"
            st.error("No se encontró la imagen BI.png")
        
        st.markdown("#### Business Intelligence")
        st.write("Potenciamos tus decisiones con visualizaciones claras y modelos de datos robustos.")

# 5.2. Cuadro 2: Inteligencia Artificial (con imagen clickable)
with col_ia:
    with st.container(border=True):
        if img_ia_b64:
            # Usamos tu URL actualizada para agentssmartenterprice
            st.markdown(
                f"""
                <a href='https://agentssmartenterprice-gspen5mrkzof7fzqbmatys.streamlit.app/' target='_blank'>
                    <img src='data:image/png;base64,{img_ia_b64}' width='250' style='display: block; margin-left: auto; margin-right: auto;'>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            # Mensaje de error si no se encuentra la imagen "IA.png"
            st.error("No se encontró la imagen IA.png")

        st.markdown("#### Inteligencia Artificial")
        st.write("Implementamos agentes de IA y modelos predictivos para automatizar y optimizar procesos.")

st.divider() # Otro separador visual

# --- 6. SUBTÍTULO "NUESTROS PRODUCTOS" ---
st.subheader("Nuestros Productos", divider="blue")

# --- 7. CUADROS "NUESTROS PRODUCTOS" (Urbox y IANA) ---
col_urbox, col_iana = st.columns(2, gap="large")

# 7.1. Cuadro 3: Urbox (con imagen clickable)
with col_urbox:
    with st.container(border=True):
        if img_urbox_b64:
            # Usamos tu URL actualizada para urbox.com.co
            st.markdown(
                f"""
                <a href='https://urbox.com.co/' target='_blank'>
                    <img src='data:image/png;base64,{img_urbox_b64}' width='250' style='display: block; margin-left: auto; margin-right: auto;'>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen urbox.png")

        st.markdown("#### Urbox")
        st.write("Nuestra plataforma modular para la gestión inteligente de servicios públicos.")

# 7.2. Cuadro 4: IANA (con imagen clickable)
with col_iana:
    with st.container(border=True):
        if img_iana_b64:
            # Usamos tu URL actualizada para iana-datainsightsco.com
            st.markdown(
                f"""
                <a href='https://iana-datainsightsco.com/' target='_blank'>
                    <img src='data:image/png;base64,{img_iana_b64}' width='250' style='display: block; margin-left: auto; margin-right: auto;'>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen IANA.png")

        st.markdown("#### IANA")
        st.write("Agente de IA conversacional para el análisis y gestión de datos empresariales.")

import streamlit as st
import base64
from pathlib import Path

# --- FUNCIÓN AUXILIAR PARA CONVERTIR IMÁGENES A BASE64 ---
def get_image_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Error: No se pudo encontrar la imagen en la ruta: {file_path}")
        return None
    except Exception as e:
        st.error(f"Error al cargar la imagen {file_path}: {e}")
        return None

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Datainsights Colombia",
    page_icon="logo_datai.png",
    layout="wide"
)

# --- 8. SIDEBAR ---
with st.sidebar:
    st.title("DataInsights Colombia")
    
    st.image("foto1.png") 
    st.markdown("**Oscar Javier Carabali Portela**")
    st.caption("CEO & Co-Fundador") 
    
    st.divider()
    
    st.image("foto2.png")
    st.markdown("**John Alexander Zapata Ortiz**")
    st.caption("CTO & Co-Fundador") 
    
    st.divider()
    
    st.caption("© Datainsights Colombia 2025. \nTodos los derechos reservados.")

# --- PRE-CARGAR IMÁGENES COMO BASE64 ---
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

st.divider()

# --- 4. SUBTÍTULO "Nuestra Esencia" ---
st.subheader("Nuestra Esencia", divider="blue")

# --- 5. CUADROS "QUÉ HACEMOS" (B.I. y I.A.) ---
col_bi, col_ia = st.columns(2, gap="large") 

# 5.1. Cuadro 1: Business Intelligence (con imagen clickable)
with col_bi:
    # ELIMINAMOS 'border=True' DE st.container()
    with st.container(): 
        if img_bi_b64:
            st.markdown(
                f"""
                <a href='https://url-para-bi.com' target='_blank' style='text-decoration: none;'>
                    <div style='display: flex; justify-content: center; align-items: center; min-height: 200px;'> 
                        <img src='data:image/png;base64,{img_bi_b64}' width='250' style='max-width: 100%; height: auto; display: block;'>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen BI.png")
        
        st.markdown("<h4 style='text-align: center;'>Business Intelligence</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Potenciamos tus decisiones con visualizaciones claras y modelos de datos robustos.</p>", unsafe_allow_html=True)

# 5.2. Cuadro 2: Inteligencia Artificial (con imagen clickable)
with col_ia:
    # ELIMINAMOS 'border=True' DE st.container()
    with st.container():
        if img_ia_b64:
            st.markdown(
                f"""
                <a href='https://agentssmartenterprice-gspen5mrkzof7fzqbmatys.streamlit.app/' target='_blank' style='text-decoration: none;'>
                    <div style='display: flex; justify-content: center; align-items: center; min-height: 200px;'>
                        <img src='data:image/png;base64,{img_ia_b64}' width='250' style='max-width: 100%; height: auto; display: block;'>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen IA.png")

        st.markdown("<h4 style='text-align: center;'>Inteligencia Artificial</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Implementamos agentes de IA y modelos predictivos para automatizar y optimizar procesos.</p>", unsafe_allow_html=True)

st.divider()

# --- 6. SUBTÍTULO "NUESTROS PRODUCTOS" ---
st.subheader("Nuestros Productos", divider="blue")

# --- 7. CUADROS "NUESTROS PRODUCTOS" (Urbox y IANA) ---
col_urbox, col_iana = st.columns(2, gap="large")

# 7.1. Cuadro 3: Urbox (con imagen clickable)
with col_urbox:
    # ELIMINAMOS 'border=True' DE st.container()
    with st.container():
        if img_urbox_b64:
            st.markdown(
                f"""
                <a href='https://urbox.com.co/' target='_blank' style='text-decoration: none;'>
                    <div style='display: flex; justify-content: center; align-items: center; min-height: 200px;'>
                        <img src='data:image/png;base64,{img_urbox_b64}' width='250' style='max-width: 100%; height: auto; display: block;'>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen urbox.png")

        st.markdown("<h4 style='text-align: center;'>Urbox</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Nuestra plataforma modular para la gestión inteligente de servicios públicos.</p>", unsafe_allow_html=True)

# 7.2. Cuadro 4: IANA (con imagen clickable)
with col_iana:
    # ELIMINAMOS 'border=True' DE st.container()
    with st.container():
        if img_iana_b64:
            st.markdown(
                f"""
                <a href='https://iana-datainsightsco.com/' target='_blank' style='text-decoration: none;'>
                    <div style='display: flex; justify-content: center; align-items: center; min-height: 200px;'>
                        <img src='data:image/png;base64,{img_iana_b64}' width='250' style='max-width: 100%; height: auto; display: block;'>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No se encontró la imagen IANA.png")

        st.markdown("<h4 style='text-align: center;'>IANA</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Agente de IA conversacional para el análisis y gestión de datos empresariales.</p>", unsafe_allow_html=True)


import streamlit as st

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
    st.image("foto1.png")
    st.markdown("**Oscar Javier Carabali Portela**")
    st.caption("CEO & Co-Fundador") # (Puedes añadir un caption si quieres)
    
    st.divider() # Separador
    
    # 8.3. Foto 2 y Nombre
    st.image("foto2.png")
    st.markdown("**John Alexander Zapata Ortiz**")
    st.caption("CTO & Co-Fundador") # (Puedes añadir un caption si quieres)
    
    st.divider() # Separador
    
    # 8.4. Derechos reservados
    st.caption("© Datainsights Colombia 2025. \nTodos los derechos reservados.")

# --- CUERPO PRINCIPAL DE LA PÁGINA ---

# --- 1. LOGO EN CABECERA CENTRADO ---
# Creamos 3 columnas, la del medio (col2) será más ancha y contendrá el logo
col1, col2, col3 = st.columns([1, 2, 1]) # Proporción 1:2:1
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
col_bi, col_ia = st.columns(2, gap="large") # Dos columnas con un espacio grande entre ellas

# 5.1. Cuadro 1: Business Intelligence
with col_bi:
    # Usamos st.container(border=True) para crear un efecto de "tarjeta"
    with st.container(border=True):
        st.image("B.I.png")
        st.markdown("#### Business Intelligence")
        st.write("Potenciamos tus decisiones con visualizaciones claras y modelos de datos robustos.")
        # Reemplaza la URL por la correcta
        st.link_button("Conoce más de B.I.", "https://url-para-bi.com") 

# 5.2. Cuadro 2: Inteligencia Artificial
with col_ia:
    with st.container(border=True):
        st.image("I.A.png")
        st.markdown("#### Inteligencia Artificial")
        st.write("Implementamos agentes de IA y modelos predictivos para automatizar y optimizar procesos.")
        # Reemplaza la URL por la correcta
        st.link_button("Conoce más de I.A.", "https://url-para-ia.com")

st.divider() # Otro separador visual

# --- 6. SUBTÍTULO "NUESTROS PRODUCTOS" ---
st.subheader("Nuestros Productos", divider="blue")

# --- 7. CUADROS "NUESTROS PRODUCTOS" (Urbox y IANA) ---
col_urbox, col_iana = st.columns(2, gap="large")

# 7.1. Cuadro 3: Urbox
with col_urbox:
    with st.container(border=True):
        st.image("urbox.png")
        st.markdown("#### Urbox")
        st.write("Nuestra plataforma modular para la gestión inteligente de servicios públicos.")
        # Reemplaza la URL por la correcta
        st.link_button("Ir a Urbox", "https://url-para-urbox.com")

# 7.2. Cuadro 4: IANA
with col_iana:
    with st.container(border=True):
        st.image("IANA.png")
        st.markdown("#### IANA")
        st.write("Agente de IA conversacional para el análisis y gestión de datos empresariales.")
        # Reemplaza la URL por la correcta
        st.link_button("Ir a IANA", "https://url-para-iana.com")
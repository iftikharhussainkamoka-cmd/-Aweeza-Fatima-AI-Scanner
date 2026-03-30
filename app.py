import streamlit as st
import pytesseract
from PIL import Image

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Page Config
st.set_page_config(page_title="AI Smart Scanner", page_icon="🔍")

# Optimization: Taake app crash na ho
@st.cache_resource
def get_tesseract_version():
    try:
        return pytesseract.get_tesseract_version()
    except:
        return "Unknown"

st.title("🔍 AI Smart Mobile Scanner")

# Language Selection
lang_option = st.selectbox("Select Language / Zaban chunein:", ("English", "Urdu"))
lang_code = 'eng' if lang_option == "English" else 'urd'

uploaded_file = st.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with st.spinner('Scanning... Please wait'):
            # OCR Process
            text = pytesseract.image_to_string(image, lang=lang_code)
            
            if text.strip():
                st.success("Done!")
                if lang_code == 'urd':
                    st.markdown(f'<p style="text-align: right; font-size: 22px; direction: rtl; background-color: #f0f2f6; padding: 15px; border-radius: 5px; color: black;">{text}</p>', unsafe_allow_html=True)
                else:
                    st.text_area("Extracted Text:", text, height=250)
                
                st.download_button("Download Text", text, file_name="scan.txt")
            else:
                st.warning("No text found. Make sure the image is clear.")
    except Exception as e:
        st.error(f"Error: {e}. Try refreshing the page.")

st.caption("Developed by Aweeza Fatima")

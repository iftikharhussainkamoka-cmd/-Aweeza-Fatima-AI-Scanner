import streamlit as st
import pytesseract
from PIL import Image

# Tesseract Configuration
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Page Setup
st.set_page_config(page_title="AI Multi-Lang Scanner", page_icon="🔍", layout="centered")

st.title("🔍 AI Smart Mobile Scanner")
st.subheader("Scan English & Urdu text instantly")

# Language Selection Dropdown
lang_option = st.selectbox("Select Language / Zaban chunein:", ("English", "Urdu"))
lang_code = 'eng' if lang_option == "English" else 'urd'

st.markdown("---")

# Image Upload
uploaded_file = st.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    st.write(f"### Scanning in {lang_option}...")
    
    try:
        extracted_text = pytesseract.image_to_string(image, lang=lang_code)
        
        if extracted_text.strip():
            st.success("Scanning Complete!")
            if lang_code == 'urd':
                st.markdown(f'<p style="text-align: right; font-size: 22px; direction: rtl; background-color: #f0f2f6; padding: 20px; border-radius: 10px; color: black;">{extracted_text}</p>', unsafe_allow_html=True)
            else:
                st.text_area("Extracted Text:", extracted_text, height=300)
            
            st.download_button("Download Text", extracted_text, file_name="scanned_text.txt")
        else:
            st.warning("No text detected. Try a clearer image.")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Developed by Aweeza Fatima | Software Engineering Project")

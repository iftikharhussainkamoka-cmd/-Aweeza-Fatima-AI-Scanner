import streamlit as st
import pytesseract
from PIL import Image

# Path for Streamlit Cloud
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

st.set_page_config(page_title="AI Smart Scanner", page_icon="🔍")

st.title("🔍 AI Smart Mobile Scanner")
st.write("Upload a clear photo of English text to scan.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    with st.spinner('Scanning text...'):
        try:
            # Simple English OCR
            text = pytesseract.image_to_string(image)
            if text.strip():
                st.success("Scanning Successful!")
                st.text_area("Extracted Text:", text, height=250)
                st.download_button("Download Text", text, file_name="scanned_text.txt")
            else:
                st.warning("No text found. Try a clearer photo.")
        except Exception as e:
            st.error(f"Error: {e}")

st.caption("Developed by Aweeza Fatima | Software Engineering Project")

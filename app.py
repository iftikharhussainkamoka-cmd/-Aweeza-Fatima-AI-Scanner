import streamlit as st
import pytesseract
from PIL import Image
import io

# Tesseract Configuration
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Page Branding
st.set_page_config(page_title="AI Smart Scanner", page_icon="🔍", layout="centered")

st.title("🔍 AI Smart Mobile Scanner")
st.markdown("---")

# 1. Image Upload Section
uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Display Preview
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Document Preview', use_container_width=True)
    
    # 2. Action Button
    if st.button('✨ START AI SCANNING'):
        with st.spinner('AI is analyzing the text... Please wait.'):
            # OCR Processing
            extracted_text = pytesseract.image_to_string(image)
            
            if extracted_text.strip():
                st.success("Analysis Complete!")
                
                # 3. Result Display
                st.subheader("Extracted Text Output:")
                st.text_area("You can copy the text below:", extracted_text, height=300)
                
                # 4. Download Option
                st.download_button(
                    label="📥 Download Results as Text File",
                    data=extracted_text,
                    file_name="scanned_result.txt",
                    mime="text/plain"
                )
            else:
                st.error("No readable text found. Please try a clearer photo.")

st.markdown("---")
st.info("Note: Ensure your mobile and laptop are on the same Wi-Fi network to use the 'Network URL'.")
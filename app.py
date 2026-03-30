import streamlit as st
import pytesseract
from PIL import Image
import io

# 1. Tesseract Configuration for Streamlit Cloud (Linux)
# This path is required for the cloud server to find the OCR engine
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# 2. Page Setup
st.set_page_config(page_title="AI Smart Scanner", page_icon="🔍", layout="centered")

st.title("🔍 AI Smart Mobile Scanner")
st.subheader("Convert images to text instantly")
st.markdown("---")

# 3. Image Upload Section
uploaded_file = st.file_uploader("Choose an image (JPG, PNG, JPEG)...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    st.write("### Processing Image...")
    
    try:
        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image)
        
        if extracted_text.strip():
            st.success("Scanning Complete!")
            st.text_area("Extracted Text:", extracted_text, height=300)
            
            # Download button for the text
            st.download_button(
                label="Download Text as File",
                data=extracted_text,
                file_name="scanned_text.txt",
                mime="text/plain"
            )
        else:
            st.warning("No text detected. Please upload a clearer image.")
            
    except Exception as e:
        st.error(f"System Error: {e}")
        st.info("Technical Tip: Ensure 'packages.txt' exists in your GitHub with 'tesseract-ocr' written inside.")

st.markdown("---")
st.caption("Developed by Aweeza Fatima | Software Engineering Project")

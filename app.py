import streamlit as st
import pytesseract
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI Halal Scanner")

st.title("AI Halal Verification Scanner")
st.markdown("##### *Automated AI Analysis for Halal Compliance*")
st.write("Upload a photo...")
haram_ingredients = [
    "e120", "e441", "gelatin", "lard", "pepsin", 
    "shortening", "bacon", "pork", "alcohol", "carmine"
]

# 2. Image Upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    with st.spinner('Scanning ingredients...'):
        # 3. Extract Text (OCR)
        extracted_text = pytesseract.image_to_string(image)
        st.subheader("Extracted Text:")
        st.write(extracted_text)
        
        # 4. Halal/Haram Logic
        found_haram = []
        text_lower = extracted_text.lower()
        
        for ingredient in haram_ingredients:
            if ingredient in text_lower:
                found_haram.append(ingredient)
        
        st.divider()
        
        # 5. Show Results
        if found_haram:
            st.error(f"⚠️ CAUTION: Haram/Mushkook ingredients detected: {', '.join(found_haram)}")
            st.warning("Please verify the source of these ingredients (e.g., Plant vs Animal based).")
        else:
            st.success("✅ No Haram ingredients from our database were detected.")
            st.info("Note: Always check for a certified Halal logo on the packaging.")

st.sidebar.info("This AI tool uses OCR to identify potential non-halal ingredients in processed foods.")

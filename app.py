import streamlit as st
import requests
from PIL import Image
import io

# FastAPI Backend URL
FASTAPI_URL = "http://127.0.0.1:8000/analyze-soil/"

st.title("AgriSense - Soil Analysis")
st.write("Upload a soil image to get crop recommendations.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Send request to FastAPI
    if st.button("Analyze Soil"):
        with st.spinner("Analyzing..."):
            try:
                files = {"file": ("soil_image.jpg", img_bytes, "image/jpeg")}
                response = requests.post(FASTAPI_URL, files=files, timeout=10)

                if response.status_code == 200:
                    result = response.json()
                    recommended_crop = result.get("recommended_crop", "N/A")
                    st.success(f"🌱 Recommended Crop: {recommended_crop}")
                else:
                    st.error(f"⚠️ Error {response.status_code}: {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Request failed: {e}")

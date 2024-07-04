import streamlit as st
from rembg import remove
from PIL import Image
import io

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        border-radius: 8px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stFileUploader {
        border: 2px dashed #ccc;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("BG removal byte bite ")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        st.write("Removing background...")
        result = remove(image)
        
        st.image(result, caption='Image with Background Removed', use_column_width=True)
        
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="output.png",
            mime="image/png"
        )

        st.success("Background Removed Successfully")

if __name__ == "__main__":
    main()

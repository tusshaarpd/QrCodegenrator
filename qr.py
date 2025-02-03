import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(data):
    """Generate QR code from input data"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.set_page_config(page_title="QR Code Generator", page_icon="🔲")
    st.title("🔲 Instant QR Code Generator")
    
    # User input
    input_data = st.text_input(
        "Enter URL or text:",
        placeholder="https://example.com or any text",
        key="qr_input"
    )
    
    # Generate QR code
    if input_data:
        try:
            qr_img = generate_qr_code(input_data)
            
            # Convert to bytes for display and download
            img_bytes = io.BytesIO()
            qr_img.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            
            # Display QR code
            st.image(img_bytes, caption="Generated QR Code", use_column_width=False)
            
            # Download button
            st.download_button(
                label="Download QR Code",
                data=img_bytes,
                file_name="qrcode.png",
                mime="image/png"
            )
            
        except Exception as e:
            st.error(f"Error generating QR code: {str(e)}")
    else:
        st.info("👆 Enter text or URL above to generate QR code")

if __name__ == "__main__":
    main()

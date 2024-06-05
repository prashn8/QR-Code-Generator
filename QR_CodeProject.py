import qrcode
from PIL import Image, ImageDraw
import os

def generate_custom_qr(data, save_path):
    # Create instance of QRCode
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image with a colored background
    qr_img = qr.make_image(fill_color="black", back_color="yellow")
    
    # Add a border around the QR code
    border_size = 20
    border_color = "yellow"
    qr_img_with_border = Image.new("RGB", (qr_img.size[0] + border_size * 2, qr_img.size[1] + border_size * 2), border_color)
    qr_img_with_border.paste(qr_img, (border_size, border_size))

    # Save the QR code image
    qr_img_with_border.save(save_path)
    print(f"Custom QR code saved to {save_path}")

if __name__ == "__main__":
    # Data for the QR code
    qr_data = "https://replit.com/@prashanttiwar39/QRCode-generator-project-1"
    
    # Path to save the QR code image
    save_path = os.path.join(os.getcwd(), "Custom_QR_Code.png")
    
    # Generate the custom QR code
    generate_custom_qr(qr_data, save_path)


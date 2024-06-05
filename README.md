# Custom QR Code Generator

Custom QR Code Generator is a Python project that creates a QR code with a custom background color and border. The generated QR code can encode URLs or other data, making it easy to share information visually.

## Features

- Generate a QR code with customizable colors.
- Add a border around the QR code.
- Save the QR code as an image file.

## Installation

To use the Custom QR Code Generator, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/prashn8/CustomQRCodeGenerator.git
2. Navigate to the project directory:
cd CustomQRCodeGenerator
3. Install the required dependencies:
pip install qrcode[pil] Pillow

## Usage
Once the project is set up, you can generate a custom QR code by running the script.

Running the Project

1. Modify the qr_data variable in the script with the data you want to encode in the QR code:
qr_data = "https://your-url-here"
2. Run the script:
python custom_qr_code_generator.py

## Example
The example below demonstrates how to generate a QR code with a URL and save it as an image:

1. Update the qr_data variable with your desired URL or data:
qr_data = "https://replit.com/@prashanttiwar39/QRCode-generator-project-1"

3. Run the script:
python custom_qr_code_generator.py

3. The script will generate a QR code with a black foreground, yellow background, and a yellow border, and save it as Custom_QR_Code.png in the current directory.
Custom QR code saved to /path/to/your/directory/Custom_QR_Code.png

## Project Structure

CustomQRCodeGenerator/
├── custom_qr_code_generator.py
├── Custom_QR_Code.png (generated file)
├── README.md

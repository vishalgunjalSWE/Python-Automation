# Make sure to install the pyqrcode library:
# pip install pyqrcode
# pip install pypng  # Required for saving as PNG

import pyqrcode
from pyqrcode import QRCode
import png  # Required for PNG export

# Define the URL or string to be encoded in the QR code
url_string = "https://vishalgunjalswe.vercel.app/"

# Generate the QR code
qr_code = pyqrcode.create(url_string)

# Save the QR code as an SVG file
qr_code.svg("myqr.svg", scale=8)
print("QR code saved as 'myqr.svg'.")

# Save the QR code as a PNG file (requires pypng)
qr_code.png("myqr.png", scale=8)
print("QR code saved as 'myqr.png'.")

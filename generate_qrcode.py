import qrcode

import generate_qrcode
from PIL import Image

data = input("Enter anything to generate QR: ")
qr = qrcode.QRCode(version=3, box_size=8, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="aqua")

image.save("qr_code.png")
image.show()  # Display the image

# from pyzbar.pyzbar import decode
# from PIL import Image

# img = Image.open(
#     'D:/Odin_FullStack/13_Python_Projects/05_Python_Project_QR/folderQr/pikachu.png')
# result = decode(img)
# print(result)


# # import qrcode

# # data = '  Don\'t forget to generate a qr'

# # qr=qrcode.QRCode(version=1, box_size=10, border=5)

# # qr.add_data(data)
# # qr.make(fit=True)
# # img = qr.make_image(fill_color  = 'red', back_color = 'white')
# # img.save('D:/Odin_FullStack/13_Python_Projects/05_Python_Project_QR/folderQr/myqrCode.png')

# # img = qrcode.make(data)

# # img.save('D:/Odin_FullStack/13_Python_Projects/05_Python_Project_QR/folderQr/myqrCode.png')

import qrcode
from PIL import Image

# Define the data to encode
data = "I'm Pikachu!"

# Create a QR code object with custom settings
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code object
qr.add_data(data)

# Generate the QR code matrix
qr.make(fit=True)

# Create an image object from the QR code matrix, using Pikachu image as a template
pikachu_image = Image.open(
    "D:/Odin_FullStack/13_Python_Projects/05_Python_Project_QR/folderQr/pikachu.png").convert("RGBA")
qr_image = qr.make_image(fill_color="yellow", back_color=(
    255, 255, 255, 0)).convert("RGBA")
pikachu_image.paste(qr_image, (55, 140), qr_image)

# Save the resulting image as a PNG file
pikachu_image.save(
    "D:/Odin_FullStack/13_Python_Projects/05_Python_Project_QR/folderQr/pikachu_qr.png")

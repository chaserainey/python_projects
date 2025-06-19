import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.CaterNaturals.com')

img = qr.make_image(fill_color="black", back_color="white", shape="square")
img.save('CaterNaturalsqrcode.png')
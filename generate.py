import qrcode

home_assistant_url = "http://homeassistant:8123/add_item"

item_to_add = "Bread"

# Construct the URL
url = f"{home_assistant_url}?item={item_to_add}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("add_item_to_shopping_list.png")

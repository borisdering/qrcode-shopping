import qrcode

home_assistant_url = "http://homeassistant:8123/api/services/shopping_list/add_item"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0MjViODAyMTg0NDI0ZTU3OGE4Y2M3NmI2YzZhNWU3MSIsImlhdCI6MTY5MzY1MTg0NywiZXhwIjoyMDA5MDExODQ3fQ.uMvkzYB5oA2s-o3OtYi1sHFrpc7fQ_Gv3GuGUM-AVf8"
item_to_add = "Bread"

# Construct the URL
url = f"{home_assistant_url}?item={item_to_add}&access_token={access_token}"

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

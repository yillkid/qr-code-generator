import qrcode

def qr_code_generate(qr_code_url):
    # Generating QR Code
    img = qrcode.make(qr_code_url)

    # Save to file
    img.save("qrcode.png")

# Example
# qr_code_generate("http://www.google.com")

# Python 3 example demonstrating multiple base encodings
import base64

data = b"Hello, Python!"

# Base16 (Hex)
hex_encoded = base64.b16encode(data)
hex_decoded = base64.b16decode(hex_encoded)

# Base32
b32_encoded = base64.b32encode(data)
b32_decoded = base64.b32decode(b32_encoded)

# Base64
b64_encoded = base64.b64encode(data)
b64_decoded = base64.b64decode(b64_encoded)

# Base85 (Ascii85)
b85_encoded = base64.b85encode(data)
b85_decoded = base64.b85decode(b85_encoded)

print("Base16:", hex_encoded, hex_decoded)
print("Base32:", b32_encoded, b32_decoded)
print("Base64:", b64_encoded, b64_decoded)
print("Base85:", b85_encoded, b85_decoded)

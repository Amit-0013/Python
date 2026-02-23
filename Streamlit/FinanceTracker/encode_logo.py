import base64

logo_path = r"C:\Users\HP\OneDrive\Desktop\LOGO.jpeg"
with open(logo_path, "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()

logo_uri = f"data:image/jpeg;base64,{b64}"

# Save to a Python file for easy import
with open("logo_base64.py", "w") as out:
    out.write(f'LOGO_URI = "{logo_uri}"\n')

print("✓ Encoded LOGO.jpeg to base64")
print(f"✓ Saved to logo_base64.py ({len(b64)} chars)")

import base64

logo_path = r"C:\Users\HP\OneDrive\Desktop\LOGO.jpeg"
with open(logo_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

# Read current FinanceTracker.py
with open(r"d:\Python\Streamlit\FinanceTracker.py", "r") as f:
    lines = f.readlines()

# Find and replace LOGO_URL line
new_lines = []
for line in lines:
    if line.startswith("LOGO_URL ="):
        new_lines.append(f'LOGO_URL = "data:image/jpeg;base64,{b64}"\n')
    else:
        new_lines.append(line)

# Write back
with open(r"d:\Python\Streamlit\FinanceTracker.py", "w") as f:
    f.writelines(new_lines)

print("✓ Embedded base64 logo into FinanceTracker.py")

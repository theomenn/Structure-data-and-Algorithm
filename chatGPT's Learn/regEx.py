import re

def extract_email_addresses(text):
    # Pola RegEx untuk mencocokkan alamat email
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    # Mencari semua kecocokan dalam teks
    matches = re.findall(email_pattern, text)

    return matches

# Contoh teks yang mengandung alamat email
sample_text = """
Abdi : abdnyc1@gmail.com
"""

# Menggunakan fungsi untuk mengekstrak alamat email dari teks
email_addresses = extract_email_addresses(sample_text)

# Menampilkan hasil
print("Alamat Email yang Ditemukan:")
for email in email_addresses:
    print(email)

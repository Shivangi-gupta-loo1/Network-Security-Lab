import subprocess

certificate = "certificate.crt"

print("X.509 CERTIFICATE ANALYZER")
print("--------------------------")

# Subject
subject = subprocess.check_output(
    ["openssl", "x509", "-in", certificate, "-noout", "-subject"],
    text=True
).strip()

# Issuer
issuer = subprocess.check_output(
    ["openssl", "x509", "-in", certificate, "-noout", "-issuer"],
    text=True
).strip()

# Validity
validity = subprocess.check_output(
    ["openssl", "x509", "-in", certificate, "-noout", "-dates"],
    text=True
).strip()

# SHA-256 Fingerprint
fingerprint = subprocess.check_output(
    ["openssl", "x509", "-in", certificate,
     "-noout", "-fingerprint", "-sha256"],
    text=True
).strip()

print(subject)
print(issuer)
print(validity)
print(fingerprint)

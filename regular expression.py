import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    email_addresses = re.findall(email_pattern, text)

    return email_addresses

sample_text = "please contact us at support@example.com or sales@example.org."
emails = extract_emails(sample_text)

print("Extracted emails:", emails)

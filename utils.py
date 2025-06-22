def is_valid_name(name):
    return name.isalpha() or " " in name

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11

def is_valid_email(email):
    return "@" in email and "." in email

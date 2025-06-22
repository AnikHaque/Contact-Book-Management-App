import csv

def load_from_file(filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_to_file(filename, contacts):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

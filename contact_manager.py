from utils import is_valid_name, is_valid_phone, is_valid_email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def load_contacts(self, data):
        self.contacts = data

    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact):
        for c in self.contacts:
            if c['phone'] == contact['phone']:
                return False, "Error: Phone number already exists for another contact."
        self.contacts.append(contact)
        return True, "Contact added successfully!"


def search_contacts(self, term):
        result = []
        term = term.lower()
        for contact in self.contacts:
            if (term in contact['name'].lower() or
                term in contact['email'].lower() or
                term in contact['phone']):
                result.append(contact)
        return result


def remove_contact(self, phone):
        for i, contact in enumerate(self.contacts):
            if contact['phone'] == phone:
                del self.contacts[i]
                return True
        return False
class Contact:
    contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contacts.append(self)

    @classmethod
    def printAllContacts(cls):
        for contact in Contact.contacts:
            print(contact)

    def __str__(self):
        return "Name " + self.name + ". Email " + self.email + "."
    
contact1 = Contact("William W")

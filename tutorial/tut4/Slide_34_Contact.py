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

    def __str__(self) -> str:
        return "Name: " + self.name + ". Email: " + self.email + "."

contact1 = Contact("Billy B", "billy.bizilis@unisa.edu.au")
contact2 = Contact("Georg G", "georg.grossmann@unisa.edu.au")

contact1.printAllContacts()
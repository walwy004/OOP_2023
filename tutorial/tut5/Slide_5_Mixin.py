class Contact:
    contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contacts.append(self)


class MailSender:
    def sendMail(self, email, message):
        print("Sending mail to: " + email)
        # <Insert email logic here...


class EmailableContact(Contact, MailSender):
    pass


emailableContact = EmailableContact("Maka Albarn", "s.eater@deathacademy.net")
emailableContact.sendMail(emailableContact.email, "Hi, you have mail.")

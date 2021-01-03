from models import database, Contact, Email
from faker import Factory

fake = Factory.create()

# Reload tables
database.drop_all()
database.create_all()
# Make 10 fake contacts
for num in range(10):
    my_email = Email(email=fake.email())

    username = fake.user_name()
    fullname = fake.name().split()
    firstname = fullname[0]
    lastname = ' '.join(fullname[1:])
    phone = fake.phone_number()

    # Save in database
    my_contact = Contact(username = username, firstname=firstname, lastname=lastname, phone=phone)
    my_contact.email.append(my_email)

    database.session.add(my_contact)
    database.session.add(my_email)

database.session.commit()

# for num in range(10):
#
#     email = fake.email()
#     # Save in database
#     my_email= Email(email=email)
#
#     database.session.add(my_email)
#
# database.session.commit()
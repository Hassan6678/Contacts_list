from models import database, Contact
from faker import Factory

fake = Factory.create()

# Reload tables
database.drop_all()
database.create_all()
# Make 10 fake contacts
for num in range(10):
    username = fake.user_name()
    fullname = fake.name().split()
    firstname = fullname[0]
    lastname = ' '.join(fullname[1:])
    phone = fake.phone_number()
    # Save in database
    my_contact = Contact(username = username, firstname=firstname, lastname=lastname, phone=phone)
    database.session.add(my_contact)

database.session.commit()

from flask import Flask, redirect, url_for, render_template, request, flash
from models import database, Contact
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretKey'
app.config['DEBUG'] = False

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)

@app.route('/')
def index():
    # Home page
    return redirect(url_for('contacts'))


@app.route("/new_contact", methods=('GET', "POST"))
def new_contact():
    form = ContactForm()

    if form.validate_on_submit():
        # create Contact Object
        my_contact = Contact()
        form.populate_obj(my_contact)
        database.session.add(my_contact)
        try:
            database.session.commit()
            flash("Contact created.", 'Success')
            return redirect(url_for('contacts'))
        except:
            database.session.rollback()
            flash('Error! ', 'Failer')

    return render_template('web/new_contact.html', form=form)

@app.route("/edit_contact/<id>",methods=('GET', 'POST'))
def edit_contact(id):
    my_contact = Contact.query.filter_by(id=id).first()
    form = ContactForm(obj=my_contact)

    if form.validate_on_submit():
        try:
            form.populate_obj(my_contact)
            database.session.add(my_contact)
            database.session.commit()

            flash('Save Successfully', 'success')
        except:
            database.session.rollback()
            flash('Error!', 'Failer')

    return render_template('web/edit_contact.html', form=form)

@app.route("/contacts")
def contacts():
    contacts = Contact.query.order_by(Contact.firstname).all()
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/search")
def search():
    name_search = request.args.get('username')

    all_contacts = Contact.query.filter(
        Contact.username.contains(name_search)
        ).order_by(Contact.firstname).all()
    return render_template('web/contacts.html', contacts=all_contacts)


@app.route("/contacts/delete", methods=('GET', 'POST'))
def contacts_delete():
    try:
        my_contact =Contact.query.filter_by(id=request.form['id']).first()
        database.session.delete(my_contact)
        database.session.commit()

        flash('Deleted.', 'success')
    except:
        database.session.rollback()
        flash('Error!', 'danger')
    return redirect(url_for('contacts'))

if __name__ == '__main__':
    app.run()

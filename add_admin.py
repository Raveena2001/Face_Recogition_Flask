# for creating an admin using python console
from app import db
from models import Faculty

def add_admin():
    admin = Faculty(name='Rav', email='rav@gmail.com', password='rav123', is_admin=True)

    db.session.add(admin)
    db.session.commit()

    print('Admin added!')
    


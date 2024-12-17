from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def init_db(app):
    # Bind the SQLAlchemy instance to the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/face'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return db

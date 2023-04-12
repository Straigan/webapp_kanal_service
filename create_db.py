from webapp import create_webapp, db

db.create_all(app=create_webapp())

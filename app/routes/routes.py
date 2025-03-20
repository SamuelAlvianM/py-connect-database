from flask import Flask
from app.connection.database import get_db
from app.models.teamlead_model import DaftarTL

def init_routes(app):
    @app.route('/add_tl')
    def add_tl():
        try:
            db = next(get_db())
            new_tl = DaftarTL(tl_name="Test TL", email="test@example.com")
            db.add(new_tl)
            db.commit()
            return "TL added successfully"
        except Exception as e:
            return f"Error adding TL: {e}"

    @app.route('/')
    def homepage():
        return "Data PostgreSQL berhasil dihubungkan!"
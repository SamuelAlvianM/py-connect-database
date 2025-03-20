from flask import Flask
from app.connection.database import init_db
from app.routes.routes import init_routes

def create_app():
    app = Flask(__name__)
    
    # Inisialisasi database
    init_db(app)
    
    # Inisialisasi routes
    init_routes(app)
    
    return app
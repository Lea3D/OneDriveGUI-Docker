from flask import Flask
from routes.profile_routes import profile_bp
from routes.sharepoint_routes import sharepoint_bp
from routes.sync_routes import sync_bp
from routes.version_routes import version_bp
from routes.settings_routes import settings_bp
from routes.maintenance_routes import maintenance_bp
from routes.gui_settings_routes import gui_settings_bp
from routes.main_routes import main_bp

def create_app():
    app = Flask(__name__)

    # Blueprints registrieren
    try:
        app.register_blueprint(profile_bp, url_prefix='/api/profile')
    except Exception as e:
        print(f"Fehler beim Registrieren von profile_bp: {e}")

    try:
        app.register_blueprint(sharepoint_bp, url_prefix='/api/sharepoint')
    except Exception as e:
        print(f"Fehler beim Registrieren von sharepoint_bp: {e}")

    try:
        app.register_blueprint(sync_bp, url_prefix='/api/sync')
    except Exception as e:
        print(f"Fehler beim Registrieren von sync_bp: {e}")

    try:
        app.register_blueprint(version_bp, url_prefix='/api/version')
    except Exception as e:
        print(f"Fehler beim Registrieren von version_bp: {e}")

    try:
        app.register_blueprint(settings_bp, url_prefix='/api/settings')
    except Exception as e:
        print(f"Fehler beim Registrieren von settings_bp: {e}")

    try:
        app.register_blueprint(maintenance_bp, url_prefix='/api/maintenance')
    except Exception as e:
        print(f"Fehler beim Registrieren von maintenance_bp: {e}")

    try:
        app.register_blueprint(gui_settings_bp, url_prefix='/api/gui-settings')
    except Exception as e:
        print(f"Fehler beim Registrieren von gui_settings_bp: {e}")

    try:
        app.register_blueprint(main_bp, url_prefix='/api/main')
    except Exception as e:
        print(f"Fehler beim Registrieren von main_bp: {e}")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

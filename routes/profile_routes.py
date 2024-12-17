from flask import Blueprint, request, jsonify
import os
import logging
import copy

# Blueprints
profile_bp = Blueprint('profile', __name__)
profile_settings_bp = Blueprint('profile_settings', __name__)
profile_status_bp = Blueprint('profile_status', __name__)

# Globale Konfiguration (Simulation)
global_config = {}
temp_global_config = {}

# === Allgemeine Profilrouten ===
@profile_bp.route('/profiles', methods=['GET'])
def list_profiles():
    """Gibt eine Liste aller Profile zurück."""
    return jsonify(list(global_config.keys())), 200

@profile_bp.route('/profiles/<profile_name>', methods=['GET'])
def get_profile(profile_name):
    """Details eines spezifischen Profils."""
    profile = global_config.get(profile_name)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    return jsonify(profile), 200

@profile_bp.route('/profiles', methods=['POST'])
def create_profile():
    """Erstellen eines neuen Profils."""
    data = request.json
    profile_name = data.get('profile_name')
    if not profile_name:
        return jsonify({"error": "Profile name is required"}), 400

    if profile_name in global_config:
        return jsonify({"error": "Profile already exists"}), 400

    global_config[profile_name] = {}
    return jsonify({"message": f"Profile '{profile_name}' created successfully."}), 201

@profile_bp.route('/profiles/<profile_name>', methods=['DELETE'])
def delete_profile(profile_name):
    """Löschen eines Profils."""
    if profile_name not in global_config:
        return jsonify({"error": "Profile not found"}), 404

    global_config.pop(profile_name)
    return jsonify({"message": f"Profile '{profile_name}' deleted successfully."}), 200

# === Profileinstellungen ===
@profile_settings_bp.route('/profiles/<profile_name>/settings', methods=['GET'])
def get_profile_settings(profile_name):
    """Abrufen der Profileinstellungen."""
    try:
        settings = global_config.get(profile_name, {})
        return jsonify(settings), 200
    except Exception as e:
        logging.error(f"Fehler beim Abrufen der Einstellungen für {profile_name}: {e}")
        return jsonify({"error": "Einstellungen konnten nicht abgerufen werden"}), 500

@profile_settings_bp.route('/profiles/<profile_name>/settings', methods=['PUT'])
def update_profile_settings(profile_name):
    """Aktualisieren der Profileinstellungen."""
    try:
        updated_settings = request.json
        temp_global_config[profile_name] = updated_settings
        global_config[profile_name] = copy.deepcopy(updated_settings)
        return jsonify({"message": "Einstellungen erfolgreich aktualisiert"}), 200
    except Exception as e:
        logging.error(f"Fehler beim Aktualisieren der Einstellungen für {profile_name}: {e}")
        return jsonify({"error": "Einstellungen konnten nicht aktualisiert werden"}), 500

# === Profilstatus ===
@profile_status_bp.route('/profile/status', methods=['GET'])
def get_profile_status():
    """Status der Profile abrufen."""
    profiles = [
        {"name": name, "has_unsaved_changes": data.get('unsaved', False)}
        for name, data in global_config.items()
    ]
    return jsonify(profiles), 200

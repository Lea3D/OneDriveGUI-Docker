from flask import Blueprint, jsonify, request
import logging

sharepoint_bp = Blueprint('sharepoint', __name__)


@sharepoint_bp.route('/api/sharepoint/sites', methods=['POST'])
def get_sharepoint_sites():
    profile_name = request.json.get("profile_name")
    if not profile_name:
        return jsonify({"error": "Profile name is required."}), 400

    try:
        # Simulate fetching SharePoint sites
        sites = ["Site A", "Site B", "Site C"]  # Placeholder for actual data
        return jsonify({"sites": sites}), 200
    except Exception as e:
        logging.error(f"Error fetching SharePoint sites: {e}")
        return jsonify({"error": "Failed to fetch SharePoint sites"}), 500


@sharepoint_bp.route('/api/sharepoint/libraries', methods=['POST'])
def get_sharepoint_libraries():
    site_name = request.json.get("site_name")
    if not site_name:
        return jsonify({"error": "Site name is required."}), 400

    try:
        # Simulate fetching SharePoint libraries
        libraries = {"Library 1": "ID1", "Library 2": "ID2"}  # Placeholder for actual data
        return jsonify({"libraries": libraries}), 200
    except Exception as e:
        logging.error(f"Error fetching SharePoint libraries: {e}")
        return jsonify({"error": "Failed to fetch SharePoint libraries"}), 500


@sharepoint_bp.route('/api/sharepoint/create-profile', methods=['POST'])
def create_library_profile():
    data = request.json
    profile_name = f"SharePoint_{data['site_name'].replace(' ', '_')}_{data['library_name'].replace(' ', '_')}"
    sync_dir = f"~/{profile_name}"
    library_id = data["library_id"]

    try:
        # Logik zum Speichern des Profils hier implementieren
        logging.info(f"Profile {profile_name} created with sync_dir {sync_dir} and drive_id {library_id}.")
        return jsonify({"message": f"Profile {profile_name} created successfully."}), 200
    except Exception as e:
        logging.error(f"Error creating profile: {e}")
        return jsonify({"error": "Failed to create profile"}), 500

from flask import Blueprint, jsonify, request
import logging
import os

settings_bp = Blueprint('settings', __name__)

# Mocked GUI Settings for demonstration
gui_settings = {
    "SETTINGS": {
        "client_bin_path": "onedrive",
        "log_file": "~/onedrive.log",
        "debug_level": "INFO",
        "start_minimized": "True",
        "frameless_window": "False",
        "combined_start_stop_button": "True",
        "QWebEngine_login": "False",
        "show_debug": "True",
        "save_debug": "False",
        "log_rotation_interval": "7",
        "log_backup_count": "5"
    }
}
GUI_SETTINGS_FILE = "gui_settings.conf"

@settings_bp.route('/api/settings/get', methods=['GET'])
def get_settings():
    return jsonify(gui_settings), 200

@settings_bp.route('/api/settings/save', methods=['POST'])
def save_settings():
    try:
        new_settings = request.json
        gui_settings["SETTINGS"].update(new_settings)
        with open(GUI_SETTINGS_FILE, "w") as f:
            for section, settings in gui_settings.items():
                f.write(f"[{section}]\n")
                for key, value in settings.items():
                    f.write(f"{key} = {value}\n")
        return jsonify({"message": "Settings saved successfully."}), 200
    except Exception as e:
        logging.error(f"Error saving settings: {e}")
        return jsonify({"error": "Failed to save settings"}), 500

@settings_bp.route('/api/settings/bin-path', methods=['POST'])
def set_bin_path():
    try:
        bin_path = request.json.get("bin_path")
        if not os.path.exists(bin_path):
            return jsonify({"error": "Specified path does not exist."}), 404
        gui_settings["SETTINGS"]["client_bin_path"] = bin_path
        return jsonify({"message": "Client binary path updated successfully."}), 200
    except Exception as e:
        logging.error(f"Error updating client binary path: {e}")
        return jsonify({"error": "Failed to update client binary path"}), 500

@settings_bp.route('/api/settings/log-dir', methods=['POST'])
def set_log_dir():
    try:
        log_dir = request.json.get("log_dir")
        if not os.path.exists(log_dir):
            return jsonify({"error": "Specified directory does not exist."}), 404
        gui_settings["SETTINGS"]["log_file"] = os.path.join(log_dir, "onedrive.log")
        return jsonify({"message": "Log directory updated successfully."}), 200
    except Exception as e:
        logging.error(f"Error updating log directory: {e}")
        return jsonify({"error": "Failed to update log directory"}), 500

from flask import Blueprint, jsonify, request
import os
import logging

gui_settings_bp = Blueprint('gui_settings', __name__)

global_config = {}  # Mocked global config for demonstration purposes
def save_global_config():
    pass  # Mocked save function for demonstration purposes

@gui_settings_bp.route('/gui/settings/start-minimized', methods=['GET', 'POST'])
def manage_start_minimized():
    if request.method == 'POST':
        state = request.json.get("state", False)
        global_config.setdefault('SETTINGS', {})['start_minimized'] = str(state)
        save_global_config()
        return jsonify({"message": "Start minimized setting updated."}), 200

    state = global_config.get('SETTINGS', {}).get('start_minimized', "False")
    return jsonify({"start_minimized": state == "True"}), 200

@gui_settings_bp.route('/gui/settings/log-file', methods=['POST'])
def set_log_file():
    log_file = request.json.get("log_file", "")
    if log_file:
        global_config.setdefault('SETTINGS', {})['log_file'] = log_file
        save_global_config()
        return jsonify({"message": "Log file path updated."}), 200
    return jsonify({"error": "Log file path cannot be empty."}), 400

@gui_settings_bp.route('/gui/settings/debug-level', methods=['POST'])
def set_debug_level():
    debug_level = request.json.get("debug_level", "INFO")
    global_config.setdefault('SETTINGS', {})['debug_level'] = debug_level
    save_global_config()
    return jsonify({"message": "Debug level updated."}), 200

@gui_settings_bp.route('/gui/settings/log-settings', methods=['POST'])
def set_log_settings():
    log_rotation_interval = request.json.get("log_rotation_interval")
    log_backup_count = request.json.get("log_backup_count")

    if log_rotation_interval is not None:
        global_config.setdefault('SETTINGS', {})['log_rotation_interval'] = str(log_rotation_interval)

    if log_backup_count is not None:
        global_config.setdefault('SETTINGS', {})['log_backup_count'] = str(log_backup_count)

    save_global_config()
    return jsonify({"message": "Log settings updated."}), 200

@gui_settings_bp.route('/gui/settings/save', methods=['POST'])
def save_settings():
    save_global_config()
    logging.info("GUI settings saved.")
    return jsonify({"message": "Settings saved successfully."}), 200

@gui_settings_bp.route('/gui/settings', methods=['GET'])
def get_all_settings():
    return jsonify(global_config.get('SETTINGS', {})), 200

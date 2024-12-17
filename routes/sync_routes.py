from flask import Blueprint, request, jsonify
import subprocess
import logging
import time
import re

sync_bp = Blueprint('sync', __name__)

@sync_bp.route('/start', methods=['POST'])
def start_sync():
    try:
        profile_name = request.json.get("profile_name", "default")
        options = request.json.get("options", "")
        command = f"onedrive --monitor {options}"

        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True
        )
        return jsonify({"message": f"Synchronization started for profile {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error starting synchronization: {e}")
        return jsonify({"error": "Failed to start synchronization"}), 500

@sync_bp.route('/stop', methods=['POST'])
def stop_sync():
    try:
        profile_name = request.json.get("profile_name", "default")
        command = "pkill -f onedrive"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": f"Synchronization stopped for profile {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error stopping synchronization: {e}")
        return jsonify({"error": "Failed to stop synchronization"}), 500

@sync_bp.route('/status/<profile_name>', methods=['GET'])
def get_sync_status(profile_name):
    try:
        # Simulierte Logik zur Rückgabe des Synchronisationsstatus
        status_message = "OneDrive sync is running"
        free_space = "10 GB"
        account_type = "Personal"

        profile_status = {
            "status_message": status_message,
            "free_space": free_space,
            "account_type": account_type,
        }
        return jsonify(profile_status), 200
    except Exception as e:
        logging.error(f"Error fetching sync status for {profile_name}: {e}")
        return jsonify({"error": "Failed to fetch sync status"}), 500

@sync_bp.route('/progress/<profile_name>', methods=['GET'])
def get_sync_progress(profile_name):
    try:
        # Simulierte Fortschrittsdaten
        progress_data = {
            "file_operation": "Downloading",
            "file_path": "~/Documents/example.txt",
            "progress": "50%",
            "transfer_complete": False,
        }
        return jsonify(progress_data), 200
    except Exception as e:
        logging.error(f"Error fetching sync progress for {profile_name}: {e}")
        return jsonify({"error": "Failed to fetch sync progress"}), 500

@sync_bp.route('/resync/<profile_name>', methods=['POST'])
def trigger_resync(profile_name):
    try:
        command = f"onedrive --resync --confdir='{profile_name}'"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": f"Resync triggered for profile {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error triggering resync for {profile_name}: {e}")
        return jsonify({"error": "Failed to trigger resync"}), 500

@sync_bp.route('/big-delete/<profile_name>', methods=['POST'])
def authorize_big_delete(profile_name):
    try:
        command = f"onedrive --confdir='{profile_name}' --big-delete"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": f"Big delete authorized for profile {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error authorizing big delete for {profile_name}: {e}")
        return jsonify({"error": "Failed to authorize big delete"}), 500

@sync_bp.route('/autostart-monitor', methods=['POST'])
def autostart_monitor():
    try:
        profiles = request.json.get("profiles", [])
        for profile_name in profiles:
            auto_sync = request.json.get("auto_sync", False)
            if auto_sync:
                start_onedrive_monitor(profile_name)
        return jsonify({"message": "Auto-sync triggered for profiles."}), 200
    except Exception as e:
        logging.error(f"Error during auto-sync: {e}")
        return jsonify({"error": "Failed to trigger auto-sync"}), 500

@sync_bp.route('/start-monitor/<profile_name>', methods=['POST'])
def start_onedrive_monitor(profile_name):
    try:
        options = request.json.get("options", "")
        command = f"onedrive --confdir='{profile_name}' --monitor {options}"
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True
        )
        return jsonify({"message": f"Monitoring started for profile {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error starting monitor for {profile_name}: {e}")
        return jsonify({"error": "Failed to start monitor"}), 500

@sync_bp.route('/resync-auth/<profile_name>', methods=['POST'])
def resync_auth_dialog(profile_name):
    try:
        command = f"onedrive --confdir='{profile_name}' --resync --resync-auth"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": f"Resync with authorization triggered for {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error triggering resync auth for {profile_name}: {e}")
        return jsonify({"error": "Failed to trigger resync auth"}), 500

@sync_bp.route('/big-delete-auth/<profile_name>', methods=['POST'])
def big_delete_auth_dialog(profile_name):
    try:
        command = f"onedrive --confdir='{profile_name}' --force"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": f"Big delete approved for {profile_name}."}), 200
    except Exception as e:
        logging.error(f"Error approving big delete for {profile_name}: {e}")
        return jsonify({"error": "Failed to approve big delete"}), 500

@sync_bp.route('/version-check', methods=['GET'])
def client_version_check():
    try:
        min_supported_version = 2500
        client_bin_path = "onedrive"

        def get_installed_client_version():
            client_version_check = subprocess.check_output([client_bin_path, "--version"], stderr=subprocess.STDOUT)
            installed_client_version = re.search(r"(v[0-9.]+)", str(client_version_check)).group(1)
            installed_client_version_num = int(installed_client_version.replace("v", "").replace(".", ""))
            installed_client_version_num = (
                installed_client_version_num
                if len(str(installed_client_version_num)) > 3
                else installed_client_version_num * 10
            )
            return installed_client_version, installed_client_version_num

        installed_client_version, installed_client_version_num = get_installed_client_version()
        if installed_client_version_num < min_supported_version:
            return jsonify({
                "message": "Unsupported OneDrive client version.",
                "installed_version": installed_client_version,
                "min_supported_version": "v2.5.0",
            }), 400

        return jsonify({
            "message": "OneDrive client version is supported.",
            "installed_version": installed_client_version,
        }), 200

    except Exception as e:
        logging.error(f"Error checking client version: {e}")
        return jsonify({"error": "Failed to check client version"}), 500

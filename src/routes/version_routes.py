from flask import Blueprint, jsonify
import subprocess
import re
import logging

version_bp = Blueprint('version', __name__)


@version_bp.route('/api/version-check', methods=['GET'])
def version_check():
    try:
        result = subprocess.run(["onedrive", "--version"], capture_output=True, text=True, check=True)
        version_output = result.stdout.strip()
        version_match = re.search(r"(v[0-9.]+)", version_output)

        if version_match:
            installed_version = version_match.group(1)
            installed_version_num = int(installed_version.replace("v", "").replace(".", ""))
            installed_version_num = (
                installed_version_num if len(str(installed_version_num)) > 3 else installed_version_num * 10
            )
            min_supported_version_num = 2500

            if installed_version_num < min_supported_version_num:
                logging.info(f"Unsupported OneDrive {installed_version} detected.")
                return jsonify({
                    "version": installed_version,
                    "status": "Unsupported",
                    "message": "Please upgrade to a supported version."
                }), 200

            logging.info(f"OneDrive {installed_version} detected.")
            return jsonify({
                "version": installed_version,
                "status": "Supported",
                "message": "OneDrive is up to date."
            }), 200
        else:
            return jsonify({"error": "Unable to parse version output."}), 500

    except FileNotFoundError:
        logging.error("OneDrive client not detected.")
        return jsonify({"error": "OneDrive client not installed. Please install it."}), 404
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking OneDrive version: {e}")
        return jsonify({"error": "Failed to get version", "details": str(e)}), 500

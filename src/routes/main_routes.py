from flask import Blueprint, jsonify, render_template, request
import logging

main_bp = Blueprint('main_routes', __name__)

@main_bp.route('/profile/new', methods=['POST'])
def create_or_import_profile():
    profile_action = request.json.get('action', 'create')
    if profile_action == 'create':
        logging.info("Profile creation initiated")
        return jsonify({"message": "Profile creation initiated"}), 200
    elif profile_action == 'import':
        logging.info("Profile import initiated")
        return jsonify({"message": "Profile import initiated"}), 200
    else:
        logging.warning("Invalid profile action")
        return jsonify({"error": "Invalid profile action"}), 400

@main_bp.route('/advanced', methods=['GET'])
def advanced_options():
    logging.info("Accessing advanced options")
    # Example backend logic or security checks could go here
    return render_template('advanced_options.html'), 200

@main_bp.route('/quit', methods=['POST'])
def quit_application():
    logging.info("Application quit")
    return jsonify({"message": "Application quit"}), 200

@main_bp.route('/', methods=['GET'])
def home():
    return render_template('main_window.html'), 200

@main_bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return '', 204

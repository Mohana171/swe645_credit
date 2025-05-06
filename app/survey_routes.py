from flask import Blueprint, request, redirect, url_for
from app.models import save_response

survey_blueprint = Blueprint('survey', __name__)

@survey_blueprint.route('/api/surveys', methods=['POST'])
def handle_survey():
    form = request.form
    save_response(form)
    return "Survey submitted successfully!"

from flask import Flask, render_template
from app.survey_routes import survey_blueprint

app = Flask(__name__)
app.register_blueprint(survey_blueprint)

@app.route('/')
def home():
    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

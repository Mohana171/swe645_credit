from app.db import conn, cursor

def save_response(form):
    query = """
        INSERT INTO survey_responses (
            first_name, last_name, street_address, city, state,
            zip_code, telephone_number, email, survey_date,
            campus_likes, interest_source, recommendation_likelihood,
            raffle_numbers, comments
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        form['firstName'],
        form['lastName'],
        form['streetAddress'],
        form['city'],
        form['state'],
        form['zip'],
        form['telephoneNumber'],
        form['email'],
        form['dateOfSurvey'],
        ','.join(form.getlist('campusLikes')),
        form['interestSource'],
        form['recommendationLikelihood'],
        form['raffle'],
        form['comments']
    )
    cursor.execute(query, values)
    conn.commit()

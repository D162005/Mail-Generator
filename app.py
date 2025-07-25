# app.py
from flask import Flask, render_template, request, jsonify
import main  # Import main.py
import mysql.connector

app = Flask(__name__)

# Establish connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Darshan@16",
    database="mailgen"
)

s1 = "generate proper mail template for"

def check_or_generate_mail_template(topic):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT template_content FROM generated_templates WHERE topic = %s", (topic,))
        template = cursor.fetchone()
        if template:
            return {'mail_content': template[0]}
        else:
            mail_content = main.generate_mail_template(topic)
            store_mail_template(topic, mail_content)
            return {'mail_content': mail_content}
    except Exception as e:
        return {'error': f'Error checking/generating mail template: {e}'}, 500
    
def check_or_generate_mail_template_from_database(topic):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT template_content FROM generated_templates WHERE topic = %s", (topic,))
        template = cursor.fetchone()
        if template:
            return {'mail_content': template[0]}
        else:
            return {'error': 'Template is not available in the database'}, 404
    except Exception as e:
        return {'error': f'Error checking/generating mail template: {e}'}, 500

def check_or_generate_mail_template_from_main(topic):
    try:
        mail_content = main.generate_mail_template(topic)
        store_mail_template(topic, mail_content)
        return {'mail_content': mail_content}
    except Exception as e:
        return {'error': f'Error generating mail template: {e}'}, 500

    except Exception as e:
        return {'error': f'Error generating mail template: {e}'}, 500

def store_mail_template(topic, mail_content):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO generated_templates (topic, template_content) VALUES (%s, %s)", (topic, mail_content))
        db.commit()
        cursor.close()
    except Exception as e:
        db.rollback()
        raise e

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.json.get('topic')
    use_database = request.json.get('use_database')
    if use_database:
        result = check_or_generate_mail_template_from_database(topic)
    else:
        result = check_or_generate_mail_template_from_main(topic)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

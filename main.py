import textwrap
from IPython.display import Markdown
import google.generativeai as genai

def to_markdown(text):
    text = text.replace('*',' *')
    return Markdown(textwrap.indent(text,'> ',predicate=lambda _:True))


def generate_mail_template(prompt):
    try:
        # Configure API key
        GOOGLE_API_KEY = "AIzaSyC6g6pabAwtmJHLwe0gVjGJEMUOH2xKSl8"
        genai.configure(api_key=GOOGLE_API_KEY)

        # Set model to 'gemini-pro'
        model_name = 'gemini-pro'
        model = genai.GenerativeModel(model_name)

        # Generate content based on user prompt
        response = model.generate_content(prompt)

        # Return the generated content
        return response.text

    except Exception as e:
        return f"Error generating mail template: {e}"

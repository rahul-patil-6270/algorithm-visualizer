from flask import Flask, render_template, request, redirect, url_for, abort
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyC7EjsWlNLMVJfLyaBkAkYkud6bo9ElQ9U")
model = genai.GenerativeModel("gemini-2.0-flash")

# Homepage
@app.route('/')
def home():
    return render_template('final_homepage.html')

# AI Assistant route
@app.route('/ai_assist', methods=['GET', 'POST'])
def ai_assist():
    response = ''
    if request.method == 'POST':
        query = request.form['query']
        result = model.generate_content(query)
        response = result.text
        return render_template('ai_assist.html', response=response, query=query)
    return render_template('ai_assist.html')

# Dynamic route to load any HTML file in templates/
@app.route('/<page_name>')
def render_any_page(page_name):
    try:
        return render_template(f'{page_name}.html')
    except:
        abort(404)

# Custom 404 page (optional)
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


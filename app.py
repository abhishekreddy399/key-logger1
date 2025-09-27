from flask import Flask, render_template
from ai_analyzer import analyze_keystrokes

app = Flask(__name__)

@app.route('/')
def index():
    report = analyze_keystrokes()
    return render_template('index.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)

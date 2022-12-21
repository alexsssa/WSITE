import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('menu_page.html')

@app.route('/OT1-page')
def OT1_page():
    return render_template('OT1-page.html')

@app.route('/OT4-page')
def OT4_page():
    return render_template('OT4-page.html')

@app.route('/OT9-page')
def OT9_page():
    return render_template('OT9-page.html')

@app.route('/OT12-page')
def OT12_page():
    return render_template('OT12-page.html')

@app.route('/OT13-page')
def OT13_page():
    return render_template('OT13-page.html')

@app.route('/OT15-page')
def OT15_page():
    return render_template('OT15-page.html')

@app.route('/OT18-page')
def OT18_page():
    return render_template('OT18-page.html')

@app.route('/OT22-page')
def OT22_page():
    return render_template('OT22-page.html')

@app.route('/OT23-page')
def OT23_page():
    return render_template('OT23-page.html')

@app.route('/OT23-page')
def OT40_page():
    return render_template('OT40-page.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
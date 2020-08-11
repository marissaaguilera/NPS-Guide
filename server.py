"""Server for NPS Guide."""

from flask import (Flask, render_template, request, flash, session, redirect)

app = Flask(__name__)



@app.route('/')
def homepage():
    """Show homepage"""

    return render_template('homepage.html')






if __name__ == '__main__':
    #connected_to_db(app)
    app.run(debug=True, host='0.0.0.0')
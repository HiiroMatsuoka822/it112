from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fortune')
def home():
    return render_template("fortune.html")
if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)



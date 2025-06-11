from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None  # Initialize result
    if request.method == 'POST':
        user = request.form['user']
        color = request.form['color']
        number = request.form['number']
        result = f"User: {user}, Favorite Color: {color}, Favorite Number: {number}"
    return render_template("fortune.html", result=result)

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

fortunes = {
    ('red', '1'): "A bold opportunity awaits you!",
    ('red', '2'): "Passion and creativity will lead you to success.",
    ('yellow', '3'): "A lucky surprise is coming your way!",
    ('blue', '4'): "Stay calm—your patience will pay off.",
    ('green', '2'): "Your kindness will bring good fortune today.",
   
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fortune', methods=['POST'])
def fortune():
    user = request.form.get('user')
    color = request.form.get('color')
    number = request.form.get('number')
    fortune_msg = fortunes.get((color, number), "Your future is mysterious!")

    return render_template('fortune.html', user=user, fortune=fortune_msg)

if __name__ == '__main__':
    app.run(debug=True)


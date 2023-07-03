from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_alpha, use_numeric, use_special):
    chars = ''
    if use_alpha:
        chars += string.ascii_letters
    if use_numeric:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "No character types selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('length'))
        use_alpha = 'alpha' in request.form
        use_numeric = 'numeric' in request.form
        use_special = 'special' in request.form
        password = generate_password(length, use_alpha, use_numeric, use_special)
        return render_template('index.html', password=password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

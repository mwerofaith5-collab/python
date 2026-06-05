from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        success = True 
    return render_template('contact.html', success=success)
if __name__ == '__main__':
    app.run(debug=True)
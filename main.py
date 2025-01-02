from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

# Add other routes as needed
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/product')
def products():
    return render_template('product.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
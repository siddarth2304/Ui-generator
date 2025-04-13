from flask import Flask, render_template, request, jsonify, send_file
from jinja2 import Template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    brand_color = request.form['brandColor']
    font = request.form['font']
    description = request.form['description']
    image = request.files['productImage']

    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    web_path = f'/static/uploads/{filename}'

    # Generate HTML code
    html_code = f'''
    <section style="font-family: {font}; background: #f9f9f9; padding: 2rem; text-align: center;">
        <img src="{web_path}" alt="Product" style="max-width: 300px; border-radius: 1rem;" />
        <h1 style="color: {brand_color};">Our Featured Product</h1>
        <p style="font-size: 1.2rem;">{description}</p>
        <button style="padding: 0.8rem 1.5rem; font-size: 1rem; background: {brand_color}; color: white; border: none; border-radius: 0.5rem;">Shop Now</button>
    </section>
    '''

    jsx_code = html_code.replace('class="', 'className="')
    liquid_code = html_code.replace('{{', '{ {').replace('}}', '} }')

    return jsonify({
        'html_code': html_code,
        'jsx_code': jsx_code,
        'liquid_code': liquid_code
    })

if __name__ == '__main__':
    app.run(debug=True)


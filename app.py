from flask import Flask, render_template, request, jsonify, redirect, url_for
from deepface import DeepFace
import os
import numpy as np
from PIL import Image
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare1')
def compare1():
    return render_template('compare.html')

@app.route('/register', methods=['POST'])
def register():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            name = file.filename
            image_path = f'./static/registered/{name}.jpg'
            file.save(image_path)
            return redirect(url_for('index'))

    return jsonify({"error": "Invalid registration data"})

@app.route('/compare', methods=['POST'])
def compare_faces():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Both files are required'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'Both files are required'}), 400

    if file1 and file2:
        # Load the uploaded images using Pillow
        image1 = Image.open(file1).convert('RGB')
        image2 = Image.open(file2).convert('RGB')

        # Convert images to numpy arrays
        image1_array = np.array(image1)
        image2_array = np.array(image2)

        # Compare the two images using DeepFace library
        result = DeepFace.verify(image1_array, image2_array ,  enforce_detection=False)
        # Return a JSON response with the result
        return json.dumps({'result': str(result['verified'])})


@app.route('/recognize', methods=['POST'])
def recognize():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            uploaded_image_path = './static/temp.jpg'
            file.save(uploaded_image_path)
            
            recognized = False
            for registered_image_filename in os.listdir('./static/registered'):
                registered_image_path = os.path.join('./static/registered', registered_image_filename)

                result = DeepFace.verify(uploaded_image_path, registered_image_path, model_name='ArcFace', enforce_detection=True)
                if result['verified']:
                    recognized = True
                    break

            os.remove(uploaded_image_path)
            return jsonify({"status": "Recognized" if recognized else "Not Recognized"})

    return jsonify({"error": "Invalid recognition data"})

if __name__ == '__main__':
    app.run(debug=True)

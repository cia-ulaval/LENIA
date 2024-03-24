import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from flask import Flask, render_template, jsonify, request
from jinja2.exceptions import TemplateNotFound
from application.world import World
import numpy as np
from application.LENIA import LENIA


app = Flask(__name__)

simulation = LENIA(640, 480, 3)
UPLOAD_FOLDER = 'C:/Users/Jardan/Desktop/LENIA/Template/World'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.get('/world')
def world_get():
    simulation.nextStep()
    world_data = simulation.world.world.tolist()
    response = jsonify({'Simulation': world_data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.post('/start')
def start_simulation():
    np.set_printoptions(threshold=sys.maxsize)
    return jsonify({'Message': 'La simulation a ete demarer avec succes'})

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    # Enregistrez l'image dans un dossier sur votre serveur ou effectuez tout autre traitement nécessaire

    return jsonify({'message': 'Image uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)


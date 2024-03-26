from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)



@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/training', methods=['POST', 'GET'])
@cross_origin()
def trainingRoute():
    os.system("python main.py")
    return "Training done successfully"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictionRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(debug=True)
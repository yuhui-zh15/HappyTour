"""
Usage:
    (backend)$ CUDA_VISIBLE_DEVICES=[gpu_id] python -m webapi.main
"""

#encoding=utf-8
import time

import cv2
import numpy as np
from flask import Flask, Response
from flask import request

from model_wrapper import ModelWrapper


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    print 'uploading...'
    fin =  request.files['file']
    data = fin.read()
    img = cv2.imdecode(np.fromstring(data, dtype=np.uint8), cv2.IMREAD_COLOR)
    predicted = ModelWrapper.predict(img)
    print 'predicted:', predicted
    return app.make_response(predicted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


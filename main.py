import flask
import werkzeug
import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import datetime

model = load_model(r'C:\Users\ilyad\Diploma Python Server\my_model_09062021.h5')


def predict_digit(img):
    img_path = img
    img = image.load_img(img_path, target_size=(256, 256))
    img = img.convert('L')
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 256, 256, 1)
    res = model.predict(img)
    os.remove(img_path)
    return max(res[0])

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    now = datetime.datetime.now()
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    for_save =  str(now.microsecond)+filename
    imagefile.save(for_save)
    answer = str(round(predict_digit(for_save) * 100, 1))
    print(answer)
    return answer


app.run(host="0.0.0.0", port=5000, debug=True)

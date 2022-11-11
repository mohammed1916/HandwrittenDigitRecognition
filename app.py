from flask import Flask, render_template, request

import make_prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    # return "<h1>Test</h1>"
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imagefile']
    imgPath = "./images/"+imageFile.filename
    imageFile.save(imgPath)
    # arr = np.array([[data1, data2, data3, data4]])
    pred = make_prediction.predict()
    pred = "The digitalised output is"+pred
    return render_template('index.html', prediction=pred)


if __name__ == "__main__":
    app.run(debug=True)

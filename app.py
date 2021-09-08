from flask import Flask, json, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model('weight_pre.h5')
@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def my_form_post():
    text = request.form['text']
    text = float(text)
    result = model.predict([text]).tolist()
    result = json.dumps(result[0][0])
    result=result.split('.',1)
    result=result[0]
    return render_template('index.html',result='Predicted Weight is: '+result)

if __name__ == '__main__':
    # app.debug=True
    app.run(debug=True)
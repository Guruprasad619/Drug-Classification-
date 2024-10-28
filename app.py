from flask import Flask, render_template, request
from model import prepare_model, predict_drug

app = Flask(__name__)

# Prepare the model
model, sc = prepare_model()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = request.form['sex']
        bp = request.form['bp']
        chol = request.form['chol']
        na = float(request.form['na'])
        
        result = predict_drug(model, sc, age, sex, bp, chol, na)
        return render_template('prediction.html', result=result)
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
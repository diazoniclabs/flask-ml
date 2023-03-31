from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('new_model')

label = ['setosa','virginica','versicolor']

@app.route('/')
def student():
   return render_template('demo.html')

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
      a	= request.form['sepal-length']
      b = request.form['sepal-width']
      c = request.form['petal-length']
      d = request.form['petal-width']
      op = model.predict([[int(a),int(b),int(c),int(d)]])
      op = label[op[0]]
      return render_template("prediction.html",result = op)

if __name__ == '__main__':
   app.run(debug = True)
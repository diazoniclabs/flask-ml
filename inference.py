import joblib

model = joblib.load('new_model')

label = ['setosa','virginica','versicolor']

op = model.predict([[6.2,3.4,5.4,2.3]])

print(label[op[0]])
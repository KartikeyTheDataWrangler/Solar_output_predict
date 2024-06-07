from flask import Flask, request, render_template, redirect, url_for
import subprocess
from src.solar_prediction.config.configeration import ConfigurationManager
from src.solar_prediction.utils.common import read_object
import numpy as np

app = Flask(__name__)

model_trainer_cofig = ConfigurationManager().model_trainer_validated()
base_model_path = model_trainer_cofig.saved_base_model_path
model = read_object(file_path=base_model_path)
print(model.get_params())

@app.route('/')
def form():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form
        data = {
            'dc_power': request.form['dc_power'],
            'daily_yield': request.form['daily_yield'],
            'total_yield': request.form['total_yield'],
            'ambient_temp': request.form['ambient_temp'],
            'module_temp': request.form['module_temp'],
            'irradiation': request.form['irradiation'],
        }
        
        print(data)
        input = np.array(list(data.values()), dtype=int).reshape(1,-1)
        prediction = model.predict(input)
    
        print(prediction)
        return render_template('result.html', prediction=prediction[0])
    
    except Exception as e:
        print(f"error occured {e} ")

@app.route('/mlflow_ui')
def mlflow_ui():

    return redirect('https://dagshub.com/KartikeyTheDataWrangler/Solar_output_predict.mlflow', code=302)

if __name__ == '__main__':
    app.run(debug=True,port=5000)

from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__)

#Custom function used in the pipeline.
def add_features(X):
    X_df=pd.DataFrame(X)
    X_df['corrosivity']=X_df['Sulfate']/(X_df['Chloramines'] + 1e-5)
    X_df['Mineral_Density']=X_df['Solids']/(X_df['Conductivity'] + 1e-5)
    X_df['Disinfection_Risk']=X_df['Organic_carbon']*X_df['Chloramines']
    return X_df

#Now, Load the pipeline
model= joblib.load('PotabilityPredictor.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    pred=None
    clr=None
    if request.method == 'POST':
       form_data_dict = request.form.to_dict() 
       user_data = pd.DataFrame(form_data_dict, index=[0])
       user_data=user_data.apply(pd.to_numeric,errors='coerce')
       pred = model.predict(add_features(user_data))[0]
       if pred == 1:
           pred = "The water is Potable"
           clr='green'
       else:
           pred = "The water is Not Potable"
           clr='red'
    return render_template('index.html', prediction=pred, clr=clr)

if __name__ == '__main__':
    app.run(debug=True)
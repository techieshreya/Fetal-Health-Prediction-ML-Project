import numpy as np 
from flask import Flask, request,jsonify,render_template
import pickle
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)

scaler=pickle.load(open('scaling.pkl',"rb"))
model=pickle.load(open('fetal.pkl','rb'))



@app.route("/",methods=['GET'])
def Home():
    print("home page is called")
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

  
   float_features=[[float(x) for x in request.form.values()]]
   
 
#    print("float_features are",float_features)
#    features=[np.array(float_features)]
   
#    print("features are",features)
   y=scaler.transform(float_features)
   print("scaled are",)
   print("predicted value is ",)
   predicted_value=model.predict(y)
  
   if (predicted_value[0]==1):
       return render_template("index.html",x="Fetal health is Normal")
   elif(predicted_value[0]==2):
       return render_template("index.html",x="Fetal health is  Suspect")
   else:
       return render_template("index.html",x="Fetal health is Pathological")

       

   


if __name__=="__main__":
    app.run(debug=True)
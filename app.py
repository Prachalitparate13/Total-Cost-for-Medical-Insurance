from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Medical_Randomforest.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("htt.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # AGE
        age = int( request.form["Age"])
      

        # BMI
        bmi =int(request.form["BMI"])

        # Children
        children = int(request.form["Children"])
      
        # Sex
        Sex = request.form["Sex"]
        if(Sex=='Male'):
            male=1
        else:
            male=0
            
       # Smoker
        Smoker = request.form["Smoker"]
        if(Smoker=='Yes'):
            yes=1
        else:
            yes=0
        
        # region
        region = request.form["Region"]
        if(region=='Northeast'):
            northwest=0
            southeast=0
            southwest=0
        elif (region=='Southeast'):
            northwest=0
            southeast=1
            southwest=0

        elif (region=='Northwest'):
            northwest=1
            southeast=0
            southwest=0
            
        elif (region=='Southwest'):
            northwest=0
            southeast=0
            southwest=1

        

        

        prediction=model.predict([[
            age,
            bmi,
            children,
            male,
            northwest,
            southeast,
            southwest,
            yes
        ]])

        output=round(prediction[0],2)

        return render_template('htt.html',prediction_text="Your Total Insurance Cost is Rs. {}".format(output))


    return render_template("htt.html")




if __name__ == "__main__":
    app.run(debug=True)

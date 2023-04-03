from flask import Flask, request, render_template
from flask_cors import cross_origin
from tensorflow import keras
import numpy as np

app = Flask(__name__)

model = keras.models.load_model('regression_model.h5')



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Day 1
        price_1 = float(request.form["price_1"])
        bsr_1 = float(request.form['bsr_1'])
        profit_1 = float(request.form["profit_1"])
        session_1 = float(request.form["session_1"])
        order_1 = float(request.form["order_1"])

        # Day 2
        price_2 = float(request.form["price_2"])
        bsr_2 = float(request.form['bsr_2'])
        profit_2 = float(request.form["profit_2"])
        session_2 = float(request.form["session_2"])
        order_2 = float(request.form["order_2"])

        # Day 3
        price_3 = float(request.form["price_3"])
        bsr_3 = float(request.form['bsr_3'])
        profit_3 = float(request.form["profit_3"])
        session_3 = float(request.form["session_3"])
        order_3 = float(request.form["order_3"])

        # Day 4
        price_4 = float(request.form["price_4"])
        bsr_4 = float(request.form['bsr_4'])
        profit_4 = float(request.form["profit_4"])
        session_4 = float(request.form["session_4"])
        order_4 = float(request.form["order_4"])

        # Day 5
        price_5 = float(request.form["price_5"])
        bsr_5 = float(request.form['bsr_5'])
        profit_5 = float(request.form["profit_5"])
        session_5 = float(request.form["session_5"])
        order_5 = float(request.form["order_5"])
        print(price_2, session_2, bsr_2, profit_2, order_2)
        inputArray = [[[price_1,session_1, bsr_1, profit_1, order_1],
                          [price_2,session_2, bsr_2, profit_2, order_2],[price_3,session_3, bsr_3, profit_3, order_3],
                          [price_4,session_4, bsr_4, profit_4, order_4], [price_5,session_5, bsr_5, profit_5, order_5]]]
        
        
        print(inputArray)
        result = model.predict(inputArray)



        return render_template('index.html',prediction_text="Your Predicted price is {}".format(result[0]))


    return render_template("index.html")




if __name__ == "__main__":
    print("Veriosn: ",keras.__version__)
    app.run(debug=True)
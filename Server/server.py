from flask import Flask, request, jsonify
import util
app= Flask(__name__)

@app.route('/get_location', methods = ['GET'])
def get_location():
    
    response = jsonify({'locations': util.get_location()})
    
    response.headers.add('Access-Control-Allow-Origin','*') 
    
    return response        


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    balcony= int(request.form['balcony'])

    response = jsonify({
        'estimated_price': util.price(location,total_sqft,bath,bhk,balcony)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response




if __name__=="__main__":
    print("Starting Python Flask server For Home Price Prediction")
    util.load()
    app.run(port=8000)
'''
Flask Server
'''

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Members API Routes
@app.route('/members')
def members():
    '''Returns a list of members'''
    return {
      "members": ["Member 1", "Member 2", "Member 3"]
    }

@app.route("/api", methods=["GET", "POST"])
def add_food():
    '''Returns a list of pantry items'''
    if request.method == "POST":
        food = request.json[0]['Food']
        brand = request.json[0]['Brand']
        quantity = request.json[0]['Quantity']
        expiry = request.json[0]['Expiry']
        date_added = request.json[0]['Date_Added']

        single_item = {
            "food": food,
            "brand": brand,
            "quantity": quantity,
            "expiry": expiry,
            "date_added": date_added,
        }
        print(single_item)
        return single_item
    # require a return statement here due to the IF used above
    # return single_item
if __name__ == '__main__':
    app.run(debug=True)

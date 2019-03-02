import flask
import csv

# init
app = flask.Flask(__name__)

# config
app.config['SECRET_KEY'] = "i forget why i need this tbh"
            
# routes
@app.route('/new_items/', methods=["POST"])
def items():
    liquids = flask.request.get_json()
    response = []
    with open('resources/ingredients.csv') as f:
        r = csv.reader(f)
        for row in r:
            if set(liquids) <= set(row):
                response.append(liquids)
        
    return flask.jsonify(response)
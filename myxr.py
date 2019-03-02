import flask
import csv
import os

# init
app = flask.Flask(__name__)

# config
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "i forget why i need this tbh"
            
# routes
@app.route('/new_item/', methods=["POST"])
def items():
    liquids = flask.request.get_json()
    print(liquids)
    response = []
    with open('resources/ingredients.csv') as f:
        r = csv.reader(f)
        for row in r:
            if set(liquids) <= set(row):
                response.append(row)
        
    return flask.jsonify(response)

@app.route('/')
def index():
    return flask.render_template('MYXR.html')
import flask
from flask import Flask, request, jsonify, abort, render_template
from crud.crud_tournament import * 

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/cards', methods=['GET'])
def read_cards():
    return print('')


@app.route('/users', methods=['GET'])
def read_users():
    return print('')


@app.route('/tournaments', methods=['POST'])
@app.route('/tournaments/', methods=['POST'])
def post_tournament():
    content = request.get_json()
    return flask.jsonify(create_tournament(content['title']))


@app.route('/tournaments/', methods=['GET'])
@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    tournament_id = request.args.get('tournamentId')
    return flask.jsonify(query_tournaments(tournament_id))


@app.route('/tournaments', methods=['DELETE'])
@app.route('/tournaments/', methods=['DELETE'])
def del_tournament():
    tournament_id = request.args.get('tournamentId')
    title = request.args.get('title')
    print(tournament_id)
    try:
        return flask.jsonify(delete_tournament(tournament_id, title))
    except Exception as error:
        return jsonify({'error': error})

app.run(debug=True)
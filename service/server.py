from service.infra.repositories import InMemoryRepository
from service.parsing.event_parsing import EventParser
from service.parsing.json_manipulation import MessageRetriever, JsonEncoder

__author__ = 'novy'

#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

repository = InMemoryRepository()
event_parser = EventParser()
message_retriever = MessageRetriever()
json_encoder = JsonEncoder()

# todo:implement


@app.route('/events/', methods=['POST'])
def create_event_log():
    message = message_retriever.retrieve_message(request.json)
    event = event_parser.parse(message)
    repository.add_event(event)

    return jsonify({'event': event.json_repr()}), 201


@app.route('/events/', methods=['GET'])
def get_recent_event_logs():
    pass


@app.route('/events/category/<string:category>', methods=['GET'])
def get_recent_event_logs_by_category(category):
    pass


@app.route('/events/category/<person>', methods=['GET'])
def get_recent_event_logs_by_category(person):
    pass


if __name__ == '__main__':
    app.run(debug=True)
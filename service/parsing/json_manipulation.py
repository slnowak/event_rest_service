import json

from service.model.event import Event


__author__ = 'novy'


class MessageRetriever(object):
    def retrieve_message(self, json):
        self._validate_input_dict(json)
        return json['message']

    def _validate_input_dict(self, json):
        if not isinstance(json, dict) or not "message" in json:
            raise ValueError()


class JsonEncoder(object):
    def encode(self, events):
        self._check_argument_type(events)
        return json.dumps({"Events": self._convert_to_serializable_format(events)}, sort_keys=True, indent=2)

    def _convert_to_serializable_format(self, events):
        return [event.simple_json_repr() for event in events]

    def _check_argument_type(self, events):
        if not isinstance(events, list):
            raise ValueError()

        for possible_event in events:
            if not isinstance(possible_event, Event):
                raise ValueError()
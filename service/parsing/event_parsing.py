from service.model.event import Event

__author__ = 'novy'

from datetime import datetime


class EventParser(object):
    def __init__(self):
        super(EventParser, self).__init__()

    def parse(self, message, creation_time=datetime.now()):
        words = self._split_by_whitespace(message)
        categories = self._with_matching_prefix("#", words)
        people = self._with_matching_prefix("@", words)

        return Event(creation_time=creation_time, content=message, categories=categories, people=people)

    def _split_by_whitespace(self, sentence):
        return sentence.split()

    def _with_matching_prefix(self, prefix, words):
        with_matching_prefix = [word for word in words if word.startswith(prefix)]
        with_prefix_omitted = [word[len(prefix):] for word in with_matching_prefix]
        without_duplicates = set(with_prefix_omitted) if with_prefix_omitted else {}
        return without_duplicates
__author__ = 'novy'


class Event(object):
    def __init__(self, creation_time, content, categories, people):
        super(Event, self).__init__()
        self.creation_time = creation_time
        self.content = content
        self.categories = categories
        self.people = people

    def matches_category(self, category):
        return item_in_collection(category, self.categories)

    def matches_person(self, person):
        return item_in_collection(person, self.people)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __hash__(self, *args, **kwargs):
        return self.__dict__.__hash__


def item_in_collection(item, collection):
    return item in collection










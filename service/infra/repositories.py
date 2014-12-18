__author__ = 'novy'


class InMemoryRepository(object):
    def __init__(self):
        super().__init__()
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_latest(self):
        pass

    def get_latest_by_category(self):
        pass

    def get_latest_by_person(self):
        pass
__author__ = 'novy'


class InMemoryRepository(object):
    def __init__(self):
        super().__init__()
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_latest(self):
        inverted_list = inverse_list(self.events)
        return top_k_from(inverted_list)

    def get_latest_by_category(self, category):
        inverted_list = inverse_list(self.events)
        items_matching_category = [event for event in inverted_list if event.matches_category(category)]
        return top_k_from(items_matching_category)

    def get_latest_by_person(self, person):
        inverted_list = inverse_list(self.events)
        items_matching_person = [event for event in inverted_list if event.matches_person(person)]
        return top_k_from(items_matching_person)


def inverse_list(list_to_inverse):
    return list_to_inverse[::-1]


def top_k_from(list_to_limit, k=10):
    return list_to_limit[:k]
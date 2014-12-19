import pymongo
from service.model.event import Event

__author__ = 'novy'


def build_from(dict_repr):
    return Event(creation_time=dict_repr["Created at"], content=dict_repr["Message"],
                 categories=set(dict_repr["Categories"]), people=set(dict_repr["People"]))


class MongoRepository(object):
    def __init__(self, db, building_strategy=build_from):
        super().__init__()
        self.events = db.events
        self.building_strategy = building_strategy

    def add_event(self, event):
        self.events.insert(event.dict_repr())

    def get_latest(self, limit=10):
        return [self.building_strategy(dict_repr)
                for dict_repr in self.events
                .find()
                .sort("Created at", pymongo.DESCENDING).limit(limit)]

    def get_latest_by_category(self, category, limit=10):
        return [self.building_strategy(dict_repr)
                for dict_repr in self.events
                .find({"Categories": {"$in": [category]}})
                .sort("Created at", pymongo.DESCENDING)
                .limit(limit)]

    def get_latest_by_person(self, person, limit=10):
        return [self.building_strategy(dict_repr)
                for dict_repr in self.events
                .find({"People": {"$in": [person]}})
                .sort("Created at", pymongo.DESCENDING)
                .limit(limit)]




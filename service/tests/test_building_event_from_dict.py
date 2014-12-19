from unittest import TestCase
import datetime
from unittest.mock import Mock
from service.infra.mongo_repo import build_from
from service.model.event import Event

__author__ = 'novy'




class TestDictBuilding(TestCase):
    def setUp(self):
        super().setUp()
        
        self.date_mock = Mock(datetime)
        self.content = "content"
        self.categories = {"cat1", "cat2"}
        self.people = {"user1", "user2"}
        
        self.input_dict = {
            "Created at": self.date_mock,
            "Message": self.content,
            "Categories": list(self.categories),
            "People": list(self.people)
        }

    def test_should_build_event_properly(self):

        expected_event = Event(creation_time=self.date_mock, content=self.content,
                               categories=self.categories, people=self.people)
        
        actual_event = build_from(self.input_dict)

        self.assertEqual(actual_event, expected_event)

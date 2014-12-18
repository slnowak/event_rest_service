from unittest import TestCase
from unittest.mock import Mock
import datetime

from service.parsing.event_parsing import EventParser
from service.model.event import Event


__author__ = 'novy'


class TestEventParser(TestCase):
    def setUp(self):
        super(TestEventParser, self).setUp()
        self.object_under_test = EventParser()
        self.date_mock = Mock(datetime)

    def test_parsing_event(self):
        event_message = "Yet another event message #message #fancyhashtag @john @michael"
        expected_event = Event(creation_time=self.date_mock, content=event_message,
                               categories={"message", "fancyhashtag"}, people={"john", "michael"})

        actual_event = self.object_under_test.parse(event_message, self.date_mock)

        self.assertEqual(actual_event, expected_event)

    def test_should_not_duplicate_any_category(self):
        event_message = "Yet another event message #cat #cat @john @michael"
        expected_event = Event(creation_time=self.date_mock, content=event_message, categories={"cat"},
                               people={"john", "michael"})

        actual_event = self.object_under_test.parse(event_message, self.date_mock)

        self.assertEqual(actual_event.__dict__, expected_event.__dict__)

    def test_should_not_duplicate_any_person(self):
        event_message = "Yet another @person event message #cat #cat @person"
        expected_event = Event(creation_time=self.date_mock, content=event_message, categories={"cat"},
                               people={"person"})

        actual_event = self.object_under_test.parse(event_message, self.date_mock)

        self.assertEqual(actual_event, expected_event)

    def test_neither_category_nor_person_should_be_recognized_when_not_whitespace_separated(self):
        event_message = "Another message#tag,@person ,#tag"
        expected_event = Event(creation_time=self.date_mock, content=event_message, categories={}, people={})

        actual_event = self.object_under_test.parse(event_message, self.date_mock)

        self.assertEqual(actual_event, expected_event)
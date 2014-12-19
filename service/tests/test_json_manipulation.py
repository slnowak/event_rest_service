from unittest.case import TestCase
import datetime
from service.model.event import Event
from service.parsing.json_manipulation import JsonEncoder, MessageRetriever

__author__ = 'novy'

expected_properly_parsed_json = """{
  "Events": [
    {
      "Created at": "2012-04-05 00:00:00",
      "Message": "Content"
    },
    {
      "Created at": "2014-12-12 00:00:00",
      "Message": "Yet another content"
    }
  ]
}"""

expected_empty_json_string = """{
  "Events": []
}"""


class JsonEncodingTest(TestCase):
    def setUp(self):
        super().setUp()
        self.object_under_test = JsonEncoder()

        self.events = [
            Event(datetime.datetime(2012, 4, 5), "Content", {"cat1", "cat2"}, {"all"}),
            Event(datetime.datetime(2014, 12, 12), "Yet another content", {"cat"}, {"all, john"}),
        ]

    def test_encode_event_collection_properly_into_json(self):

        actual_json_repr = self.object_under_test.encode(self.events)

        self.assertEqual(expected_properly_parsed_json, actual_json_repr)

    def test_encoding_empty_list(self):

        actual_json_string = self.object_under_test.encode([])

        self.assertEqual(expected_empty_json_string, actual_json_string)

    def test_should_raise_an_error_given_non_event_object(self):
        list_with_non_event_type = [self.events[0], "some string"]

        self.assertRaises(ValueError, self.object_under_test.encode, list_with_non_event_type)


class MessageRetrievingTest(TestCase):
    def setUp(self):
        self.object_under_test = MessageRetriever()

    def test_should_retrieve_argument_given_proper_input(self):
        input_json = {"message": "Event message #msg"}
        expected_message = "Event message #msg"

        actual_message = self.object_under_test.retrieve_message(input_json)

        self.assertEqual(actual_message, expected_message)

    def test_should_raise_an_error_given_not_dictionary(self):
        invalid_input = ""

        self.assertRaises(ValueError, self.object_under_test.retrieve_message, invalid_input)

    def test_should_raise_an_error_when_key_is_missing(self):
        dict_with_missing_key = {"a": "b"}

        self.assertRaises(ValueError, self.object_under_test.retrieve_message, dict_with_missing_key)
import datetime
from unittest import TestCase
from unittest.mock import Mock
from service.infra.in_memory_repo import InMemoryRepository
from service.model.event import Event

__author__ = 'novy'


class TestInMemoryRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.events = [
            self._create_event({"category1", "category2", "default"}, {"all", "john"}),
            self._create_event({"default"}, {"all", "no_one"}),
            self._create_event({"category1", "cat2", "default"}, {"all"}),
            self._create_event({"cat3", "cat2", "cat1", "default"}, {"no_one", "all"}),
            self._create_event({"category1", "cat", "default"}, {"all"}),
            self._create_event({"category", "default"}, {"john", "all"}),
            self._create_event({"category1", "category2", "default"}, {"mike", "john", "all"}),
            self._create_event({"category1", "category2", "category3", "default"}, {"mike", "all"}),
            self._create_event({"category3", "default"}, {"jack", "mike", "all"}),
            self._create_event({"without_default"}, {"nobody"}),
            self._create_event({"category", "default"}, {"random person", "all"}),
            self._create_event({"category", "category2", "default"}, {"all", "john"}),
            self._create_event({"category1", "category2", "default"}, {"all"}),
        ]

        self.object_under_test = InMemoryRepository()
        self.object_under_test.events = self.events

    def _create_event(self, categories, people):
        return Event(creation_time=Mock(datetime), content="", categories=categories, people=people)

    def test_should_return_recent_ten_events(self):
        expected_result = [self.events[12], self.events[11], self.events[10], self.events[9], self.events[8],
                           self.events[7], self.events[6], self.events[5], self.events[4], self.events[3],
                           ]

        actual_result = self.object_under_test.get_latest()

        self.assertEqual(actual_result, expected_result)

    def test_should_return_exactly_ten_recent_events_searching_by_category_given_more_matching(self):
        expected_result = [self.events[12], self.events[11], self.events[10], self.events[8], self.events[7],
                           self.events[6], self.events[5], self.events[4], self.events[3], self.events[2]
                           ]

        actual_result = self.object_under_test.get_latest_by_category("default")

        self.assertEqual(actual_result, expected_result)

    def test_should_return_exactly_ten_recent_events_searching_by_person_given_more_matching(self):
        expected_result = [self.events[12], self.events[11], self.events[10], self.events[8], self.events[7],
                           self.events[6], self.events[5], self.events[4], self.events[3], self.events[2]
                           ]

        actual_result = self.object_under_test.get_latest_by_person("all")

        self.assertEqual(actual_result, expected_result)

    def test_should_return_less_than_ten_events_searching_by_category_given_less_matching(self):
        expected_result = [self.events[12], self.events[7], self.events[6],
                           self.events[4], self.events[2], self.events[0]
                           ]

        actual_result = self.object_under_test.get_latest_by_category("category1")

        self.assertEqual(actual_result, expected_result)

    def test_should_return_less_than_ten_events_searching_by_person_given_less_matching(self):
        expected_result = [self.events[8], self.events[7], self.events[6]]

        actual_result = self.object_under_test.get_latest_by_person("mike")

        self.assertEqual(actual_result, expected_result)

    def test_should_return_empty_list_given_not_matching_category(self):

        self.assertEqual(self.object_under_test.get_latest_by_category("fake category"), [])

    def test_should_return_empty_list_given_not_matching_person(self):
        print (self.events[0].matches_category("category1"))
        self.assertEqual(self.object_under_test.get_latest_by_person("fake person"), [])
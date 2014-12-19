from unittest import TestCase
from unittest.mock import Mock
import datetime

from service.model.event import Event


__author__ = 'novy'


class TestEvent(TestCase):
    def setUp(self):
        super(TestEvent, self).setUp()
        self.object_under_test = Event(
            creation_time=Mock(datetime),
            content="This is a sentence #hashtag1 #hashtag2 @user1 @user2",
            categories={"hashtag1", "hashtag2"},
            people={"user1", "user2"}
        )

    def test_should_match_category_return_true_given_matching_category(self):
        matching_category = "hashtag1"
        self.assertTrue(self.object_under_test.matches_category(matching_category))

    def test_should_match_category_return_false_given_not_matching_category(self):
        not_matching_category = "random category"
        self.assertFalse(self.object_under_test.matches_category(not_matching_category))

    def test_should_match_person_return_true_given_matching_person(self):
        matching_user = "user1"
        self.assertTrue(self.object_under_test.matches_person(matching_user))

    def test_should_match_person_return_false_given_not_matching_person(self):
        not_matching_user = "random_user"
        self.assertFalse(self.object_under_test.matches_person(not_matching_user))

import unittest
from mock import Mock, patch, sentinel
from get_valid_url import QuestSearch, quest_search
from scraping_links import scraping_links

#TODO testing only the request function (NOT the class)
class TestQuestSearchFunc(unittest.TestCase):
    def setUp(self):

        # mocking

        # TODO: In case that only 1 module from a library(requests in this case) is used/imported
        # self.requests_get_patcher = patch('requests.get')

        self.requests_get_patcher = patch('get_valid_url.get')
        self.mock_requests_get = self.requests_get_patcher.start()

    def tearDown(self):
        # cleanup/unmocking
        self.requests_get_patcher.stop()

    def test_quest_search_unexpected_code_exit(self):

        # mock_requests_get <- Mock1

        # set custom mock data
        # get -> Mock1
        # get() -> Return: Mock2
        self.mock_requests_get.return_value = Mock(status_code=400)  # Mock2

        # assertion/testing
        self.assertRaises(SystemExit, quest_search, 'Against Lord Shalzaru', '#wh-comments')



    def test_quest_search_return_valid_html(self):

        expected_value = '<html><head></head><body></body></html>'
                                                  #content=sentinel.expected_html  TODO: ALTERNATIVE
        self.mock_requests_get.return_value = Mock(content=expected_value, status_code=200)

        self.assertEqual(expected_value, quest_search('Against Lord Shalzaru', '#wh-comments'))


'''
    My retarded mock implementation with net dependency:
'''

# class TestQuestSearch(unittest.TestCase):
#
#     def test_quest_search(self):
#
#         with patch.object(QuestSearch, 'quest_search') as mock_quest_search:
#             expected_value = '<html><head></head><body></body></html>'
#             r = QuestSearch('Some Quest', 'wh-comments')
#             mock_quest_search.return_value = '<html><head></head><body></body></html>'
#
#             #assert that we have valid status_code
#             self.assertEqual(r.response.status_code, 200)
#
#             #assert that we get valid HTML
#             some_request = r.quest_search()
#             self.assertEqual(some_request, expected_value)
#
#
#
#     def test_scraping_links(self):
#         pass
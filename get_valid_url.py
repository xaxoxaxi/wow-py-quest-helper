import requests
from requests import get
from sys import exit


class QuestSearch(object):
    #import pdb; pdb.set_trace()
    def __init__(self, quest_name, comment_section_element):
        self.quest_name = quest_name
        self.coment_section_element = comment_section_element
        url = 'http://db.vanillagaming.org/' + '/?search=' + self.quest_name + str(self.coment_section_element)
        self.response = requests.get(url.encode('utf-8')) #Against Lord Shalzaru#wh-comments

    def quest_search(self):
        try:
            if self.response.status_code == 200:
                return self.response.content
            raise ValueError("Error 404, page not found!")
        except Exception as e:
            print(e)
            exit(0)

''' Tazi funkciq sluji kato alternativa za mock test-a i ne se vika nik1de drugade '''

def quest_search(quest_name, coment_section_element):
    search_url = 'http://db.vanillagaming.org/'
    url = search_url + '/?search=' + quest_name + str(coment_section_element)
    try:
        r = get(url.encode('utf-8')) #Against Lord Shalzaru#wh-comments
        if r.status_code == 200:
            return r.content
        raise ValueError("Error 404, page not found!")
    except Exception as e:
        print(e)
        exit(0)

# 'Against the Hatecrest' # TODO proben quest path
# s = quest_search('Against Lord Shalzaru', '#wh-comments')
# print(s)
from bs4 import BeautifulSoup
from get_valid_url import QuestSearch
from getting_readable_text import getting_readable_text

def scraping_links(quest_name):

    #quest_name = str(raw_input('Type the name of the quest: ')) # Against Lord Shalzaru
    # TODO truden: 'A Donation of Mageweave'
    html_page = QuestSearch(quest_name, '#wh-comments')
    soup = BeautifulSoup(html_page.quest_search(), 'html.parser')

    #TODO: soup.find('div', id='...')
    try:
        text_list = soup.findAll('div', attrs={'class': "main-contents"})
        text_list = text_list[0].find_all('script')
        column_1 = text_list[0].string.strip()

        #print(str(result[1])) # LEN = 4 !!! for 'Against Lord Shalzaru'

        # for script in soup.find_all('script'):
        #     result.append(list(script)) #todo: DA no samo pri validen quest - url !!!

        readable_strings = getting_readable_text(column_1) # vr16ta list gotov za output
        # for comment in readable_strings:
        #     print(comment)
        #     user_input = raw_input('Press "y" if you want 1 more comment: ')
        #     if user_input == 'y':
        #         continue
        #     break
        return readable_strings
    except Exception:
        print("INVALID INPUT or QUEST DOES NOT EXIST")

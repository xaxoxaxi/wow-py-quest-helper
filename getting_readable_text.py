'''
Toq abort 'prerabotva' cancer-a ot comentarite ot HTML na readable string format za output!

za sega ne raboti i ne trqbva da se pipa !
'''

def getting_readable_text(text_list):

    #calibrate = text_list.find(",date:'")
    find_index_start = text_list.find("var wh_comments")
    find_index_end = text_list.find("var g_pageInf")
    smth = text_list[find_index_start:find_index_end]
    new_smth = recursive_test(smth[:])

    return new_smth

def recursive_test(smth):

    find_index_start = smth.find(",body:")
    find_index_end = smth.find(",date:")
    if find_index_start == -1:
        return []
    else:
        return [smth[find_index_start+7:find_index_end]] + recursive_test(smth[find_index_end+6:])

#TODO: Import main fileovete ot scraping links i pravim butoni; kato se dov1r6i da se pravi na .exe !
from Tkinter import *
#from sys import exit
import tkSimpleDialog
#import tkMessageBox
from scraping_links import scraping_links

root = Tk()
root.configure(bg="white")
root.title("Quest Helper")
root.geometry("800x600")

# Get comments
comments = None
smth = None

def comment_generator(comments):
    for comment in comments:
        yield comment

def quest_name():
    '''Give the quest name to the link scraper and returns list of all the comments'''
    global comments
    global smth
    name = tkSimpleDialog.askstring("QuestName", "Questnamme")
    comments = scraping_links(name)
    smth = comment_generator(comments)

def get_next_comment():
    '''Use the list of comments from quest_name() and displays them one by one'''
    global comments
    global smth
    try:
        lb_tasks.insert("end", next(smth))
    except:
        lb_tasks.insert("end", "No more comments")


lbl_title = Label(root, text="Give Quest Name", bg="white")
lbl_title.pack()

lbl_display = Label(root, text="", bg="white")
lbl_display.pack()

# lbl_input = Entry(root, width=30, )
# lbl_input.pack()

# BUTTON for quest name
btn_quest_name = Button(root, text="Quest Name", fg="black", bg="white", command=quest_name)
btn_quest_name.pack()

lbl_display = Label(root, text="", bg="white")
lbl_display.pack()

lbl_title = Label(root, text="COMMENTS", bg="white")
lbl_title.pack()


# BUTTON for next commet
btn_next_comment = Button(root, text="Next Comment", fg="black", bg="white", command=get_next_comment)
btn_next_comment.pack()

lbl_display = Label(root, text="", bg="white")
lbl_display.pack()

# Comment input screen
# TODO: I display stuff on the big window from here with lb_tasks.insert()
lb_tasks = Listbox(root,width=80, height=25)
lb_tasks.pack()

# BUTTON for exit
btn_exit = Button(root, text="Quit", fg="black", bg="white", command=sys.exit)
btn_exit.pack()


root.mainloop()
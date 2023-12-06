import json
import requests
from tkinter import *


def data():
    username = txt.get()
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    user_data_sorted = dict()
    keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
    for sort in keys:
        user_data_sorted[sort] = user_data[sort]
    print(user_data_sorted)
    with open('C:/Users/alyon\Desktop/GitProjects(nikita)/Nichita/пр12/user_data.txt', 'w') as write_file:
        json.dump(user_data_sorted, write_file)


window = Tk()
window.title('Krutko_Nikita')
window.geometry('800x600')
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Клик!", command=data)
btn.grid(column=2, row=0)
window.mainloop()


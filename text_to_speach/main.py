from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

languages = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Irish': 'ga',
    'Italian': 'it',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Spanish': 'es',
    'Swedish': 'sv',
    'Ukrainian': 'uk',
}

def on_language_select(value):
    global language
    language = languages[value]

def text_to_speech():
    text = entry.get()

    output = gTTS(text=text, lang=language, slow=False)
    output.save('play.mp3')
    entry.delete(0, END)
    os.system('mpg123 play.mp3')

entry = Entry(root)
canvas.create_window(200, 150, window=entry)

button = Button(text='Start', command=text_to_speech)
canvas.create_window(200, 180, window=button)

language_label = Label(text='Select Language:')
canvas.create_window(200, 210, window=language_label)

language_var = StringVar(root)
language_var.set('English')

language_dropdown = OptionMenu(canvas, language_var, *languages.keys(), command=on_language_select)
canvas.create_window(200, 240, window=language_dropdown)


root.mainloop()

















# text = open('test.txt', 'r').read()
# language = 'en'
# output = gTTS(text=text, lang=language, slow=False)
# output.save('output.mp3')
# os.system('mpg123 output.mp3')


# text = "Test speech! Hope this works!"
# output = gTTS(text=text, lang='en', slow=False)
# output.save('output.mp3')
# os.system('mpg123 output.mp3')




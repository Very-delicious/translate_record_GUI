import googletrans as gt
import tkinter as tk
import csv


def translate_record():
    translator = gt.Translator()
    res = translator.translate(str(inp.get()), dest='zh-tw')
    ans1.config(text='查詢結果 : '+res.text)
    with open('word_record.csv', 'a', encoding='utf-8', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow([str(inp.get()), res.text])


def ls_record():

    with open('word_record.csv', encoding='utf-8', newline='') as cf:
        rr = csv.reader(cf)
        x = ''
        for row in rr:
            x += ' '.join(row)+"\n"
    ans2.config(text='查詢過的單字 :\n'+x)


# GUI settings

win = tk.Tk()
win.geometry('500x700')
win.resizable(False, True)
win.title('translate and record')

tk.Label(win, text="Enter English words you don't know", fg='black').pack()

F1 = tk.Frame(win, height=5)
F1.pack(side=tk.TOP)

F2 = tk.Frame(win, height=100)
F2.pack(side=tk.TOP)

inp = tk.Entry(F1)
inp.pack(side=tk.LEFT)

tk.Button(F1, text="Translate and record", command=translate_record).pack(side=tk.LEFT)

ans1 = tk.Label(F2, text='')
ans1.pack(side=tk.TOP)

tk.Button(win, text="show record", command=ls_record).pack(side=tk.TOP)

ans2 = tk.Label(win, text='')
ans2.pack(side=tk.TOP)

win.mainloop()


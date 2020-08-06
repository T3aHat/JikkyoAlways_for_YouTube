# coding: utf-8

import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
from tkinter import ttk
import tkinter
from ctypes import windll


def get_comment_url():
    i = 0
    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        src = soup.find(attrs={"class": "style-scope ytd-live-chat-frame"})
        try:
            url = "https://www.youtube.com/"+str(src["src"])
            driver.get(url)
            print('Get comments from...\n'+url)
            return
        except:
            i += 1
            time.sleep(3)
            if(i > 5):
                print("Could't get comment from...\n"+str(url))


def get_newcomment():
    global results, j, comelist, cnt
    results = []
    cnt = len(comelist)
    j = 0
    soup = BeautifulSoup(driver.page_source, "html.parser")
    comelist = soup.find_all(
        "span", attrs={"id": "message", "class": "style-scope yt-live-chat-text-message-renderer"})
    for i in range(cnt, len(comelist)):
        if(comelist[i].string != None and len(comelist[i].string) < max_length):
            results.append(comelist[i].string)
    labels[0].after(duration, get_newcomment)


def move(i):
    def x():
        ww = f.winfo_width()
        labels[i].place(x=ww+lc[i], y=fontsize*(2*i-0.5))
        lc[i] -= v+len(nowdatalist[i])*acc
        if(ww+lc[i] < -labels[i].winfo_reqwidth()):  # 左端行った
            lefted[i] = True
        labels[i].after(1, move(i))
    return x


def update_comment():  # resultsを元にコメを書き換え
    global j, results, nowdatalist, colour
    k = 0
    for i in range(num_comment):
        if(k != 0 and k % (int(len(results)/(int(duration)/1000))+1) == 0):
            k += 1
            break
        if(lefted[i] == True):  # went left.So update comment
            while(j < len(results)):
                nowdatalist[i] = results[j]
                labels[i].place_forget()
                try:  # colourに例外が来た時のため
                    labels[i] = (ttk.Label(master=root, text=nowdatalist[i], font=(
                        "メイリオ", fontsize, bold), foreground=colour, background="grey"))
                except Exception as e:
                    print(e)
                    colour = "white"  # 強制初期化
                    labels[i] = (ttk.Label(master=root, text=nowdatalist[i], font=(
                        "メイリオ", fontsize, bold), foreground=colour, background="grey"))
                lc[i] = 0
                lefted[i] = False
                j += 1
                k += 1
                break

    labels[0].after(1000, update_comment)


def Change_word(f):
    def x(self):
        subf = tkinter.Tk()
        subf.wm_attributes("-topmost", True)
        subf.geometry("300x500")
        subf.title("Settings")

        bl1 = tkinter.BooleanVar(subf)
        if(bold == "bold"):
            bl1.set(True)
        else:
            bl1.set(False)
        CheckBox1 = tkinter.Checkbutton(
            subf, text="bold", variable=bl1)
        CheckBox1.pack()

        label1 = tkinter.Label(subf, text="num of comments(reccomend:10~25)")
        label1.pack()
        txt1 = tkinter.Entry(subf, width=30)
        txt1.insert(tkinter.END, num_comment)
        txt1.pack()

        label2 = tkinter.Label(subf, text="fontsize(reccomend:rec)")
        label2.pack()
        txt2 = tkinter.Entry(subf, width=30)
        txt2.insert(tkinter.END, fontsize)
        txt2.pack()

        label6 = tkinter.Label(
            subf, text="maximum length of comment(reccomend:100)")
        label6.pack()
        txt6 = tkinter.Entry(subf, width=30)
        txt6.insert(tkinter.END, max_length)
        txt6.pack()

        label3 = tkinter.Label(subf, text="velocity(reccomend:1)")
        label3.pack()
        txt3 = tkinter.Entry(subf, width=30)
        txt3.insert(tkinter.END, v)
        txt3.pack()

        label4 = tkinter.Label(subf, text="acceleration(reccomend:0.05)")
        label4.pack()
        txt4 = tkinter.Entry(subf, width=30)
        txt4.insert(tkinter.END, acc)
        txt4.pack()

        label5 = tkinter.Label(
            subf, text="colour(colour name(pink)or 8 bit RGB(#FFC0CB))")
        label5.pack()
        txt5 = tkinter.Entry(subf, width=30)
        txt5.insert(tkinter.END, colour)
        txt5.pack()

        label7 = tkinter.Label(
            subf, text="duration(reccomend:10000")
        label7.pack()
        txt7 = tkinter.Entry(subf, width=30)
        txt7.insert(tkinter.END, duration)
        txt7.pack()

        def transparency(n):
            root.attributes("-alpha", float(int(n)/100))

        label8 = tkinter.Label(
            subf, text="transparency")
        label8.pack()
        scale1 = tkinter.Scale(subf, from_=10, to=100, resolution=10,
                               tickinterval=90, orient=tkinter.HORIZONTAL, command=transparency)
        scale1.set(100)
        scale1.pack()

        button = tkinter.Button(subf, text="Apply")
        button.pack(side="right")
        button.bind("<1>", lambda word: change(
            f, bl1, txt1, txt2, txt3, txt4, txt5, txt6, txt7))

        button = tkinter.Button(subf, text="Default")
        button.pack(side="left")
        button.bind("<1>", lambda word: get_default(
            f, bl1, txt1, txt2, txt3, txt4, txt5, txt6, txt7))

        subf.mainloop()
    return x


def get_default(f, bl1, txt1,  txt2, txt3, txt4, txt5, txt6, txt7):
    txt1.delete(0, tkinter.END)
    txt1.insert(tkinter.END, 15)
    bl1.set(True)

    txt2.delete(0, tkinter.END)
    txt2.insert(tkinter.END, "rec")
    txt3.delete(0, tkinter.END)
    txt3.insert(tkinter.END, 1)
    txt4.delete(0, tkinter.END)
    txt4.insert(tkinter.END, 0.05)
    txt5.delete(0, tkinter.END)
    txt5.insert(tkinter.END, "white")
    txt6.delete(0, tkinter.END)
    txt6.insert(tkinter.END, 100)
    txt7.delete(0, tkinter.END)
    txt7.insert(tkinter.END, 10000)


def reinit(b, a):
    for i in range(b, a):
        lefted.append(True)
        lc.append(0)
        nowdatalist.append('')  # padding(改良の余地あり)
        labels.append(ttk.Label(master=root, text=nowdatalist[i], font=(
            "メイリオ", fontsize, bold), foreground=colour, background="grey"))
        labels[i].after(1, move(i))


def change(f, bl1, txt1, txt2, txt3, txt4, txt5, txt6, txt7):
    global bold, num_comment, fontsize, max_length, v, acc, colour, duration

    if(bl1.get()):
        bold = "bold"
    else:
        bold = "normal"
    if(int(txt1.get())-num_comment > 0):
        reinit(num_comment, int(txt1.get()))
    num_comment = int(txt1.get())
    if(txt2.get() == "rec"):
        i = 1
        while (True):
            labeltemp = ttk.Label(master=root, text='Changed settings!', font=(
                "メイリオ", i, bold), foreground='red', background='blue')
            labeltemp.place(x=0, y=0)
            reqheightemp = labeltemp.winfo_reqheight()
            labeltemp.place_forget()
            if(reqheightemp*num_comment > f.winfo_height()):
                fontsize = i
                break
            else:
                i += 1
    else:
        fontsize = int(txt2.get())
    v = int(txt3.get())
    acc = float(txt4.get())

    if(str(txt5.get()) == "grey"):
        colour = str("light grey")
    else:
        colour = str(txt5.get())
    max_length = int(txt6.get())
    if(int(txt7.get()) < 1000):
        duration = 1000
    else:
        duration = txt7.get()

    print("bold:"+str(bold))
    print("num_comment:"+str(num_comment))
    print("fontsize:"+str(fontsize))
    print("v:"+str(v))
    print("acc:"+str(acc))
    print("colour:"+colour)
    print("max_length:"+str(max_length))
    print("duration:"+str(duration))


def fullscreen(fs):
    def x(self):
        global fs
        if(fs):
            root.wm_attributes("-fullscreen", False)
            fs = False
        else:
            root.wm_attributes("-fullscreen", True)
            fs = True
    return x


if __name__ == '__main__':

    options = Options()
    options.add_argument('--headless')
    p = "chromedriver.exe"  # path_to_chromedriver
    driver = webdriver.Chrome(
        executable_path=p, options=options)
    url = input("Input YouTube Live URL > ")
    driver.get(url)
    cnt = 0
    get_comment_url()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    comelist = soup.find_all(
        "span", attrs={"id": "message", "class": "style-scope yt-live-chat-text-message-renderer"})
    cnt = len(comelist)
    num_comment = 20
    fontsize = 30
    v = 1
    acc = 0.05
    max_length = 100
    bold = "bold"
    colour = "white"
    fs = False
    duration = 5000
    lefted = []
    ww = windll.user32.GetSystemMetrics(0)
    wh = windll.user32.GetSystemMetrics(1)
    root = tkinter.Tk()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "grey")
    ttk.Style().configure("TP.TFrame", background="grey")
    root.title("JikkyoAlways_for_YouTube")
    f = ttk.Frame(master=root, style="TP.TFrame", width=ww, height=wh)
    root.bind("<Control-Key-s>", Change_word(f))
    root.bind("<Control-Key-f>", fullscreen(fs))
    f.pack()
    j = 0
    lc = []
    results = []
    nowdatalist = []
    labels = []
    for i in range(num_comment):
        lc.append(-ww)
        lefted.append(True)
        nowdatalist.append('')
        labels.append(ttk.Label(master=root, text='', font=(
            "メイリオ", fontsize, bold), foreground=colour, background="grey"))

    for i in range(num_comment):
        labels[i].after(1, move(i))

    get_newcomment()
    update_comment()

    root.mainloop()
    driver.close()
    driver.quit()

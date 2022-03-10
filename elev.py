import tkinter as tk
from PIL import ImageTk, Image
path = '' #closed_elev
path2 = '' #open elev
c = []; x = 245; y = 200
def Well(btn):
    c.append(btn.cget('text')); array.config(text=('Текущая очередь:\n' + ' '.join(c)))
    win.update()
def Lesss_go():
    # print(placement.cget('text').split()[-2]) / just check if something doesn't work or work incorrectly
    Move(list(set(c)))
def Move(floors):
    panel.config(image=img)
    floors.sort()
    # Think about saving elevator's position.
    f = int(kef.cget('text'))
    while len(c) != 0:
        if len(floors) > 0:
            for floor_ in floors:
                if int(floor_) == int(placement.cget('text').split()[-2]):
                    while str(int(placement.cget('text').split()[-2])) in c:
                        c.pop(c.index(str(int(placement.cget('text').split()[-2]))))
                    floors.pop(floors.index(str(int(floor_))))
                    array.config(text=('Текущая очередь:\n' + ' '.join(c)))
                    win.update()
        if len(floors) > 0 and int(floors[0]) < int(placement.cget('text').split()[-2]):
            for floor_ in range(int(placement.cget('text').split()[-2]), int(floors[0]), -1):
                placement.after(1000, placement.config(text=('Лифт находится на:\n' + str(floor_-1) + ' этаже')))
                panel.place_configure(x=x, y=f+35)
                if str(floor_-1) in floors:
                    while str(floor_-1) in c:
                        c.pop(c.index(str(floor_-1)))
                    array.config(text=('Текущая очередь:\n' + ' '.join(c)))
                    win.update()
                f += 35
                win.update()
            win.update()
        if len(floors) > 0 and int(floors[0]) > int(placement.cget('text').split()[-2]):
            for floor_ in range(int(placement.cget('text').split()[-2]), int(floors[-1])):
                placement.after(1000, placement.config(text=('Лифт находится на:\n' + str(floor_+1) + ' этаже')))
                panel.place_configure(x=x, y=f-35)
                if str(floor_+1) in floors:
                    while str(floor_+1) in c:
                        c.pop(c.index(str(floor_+1)))
                    array.config(text=('Текущая очередь:\n' + ' '.join(c)))
                    win.update()
                f -= 35
                win.update()
            win.update()
    if len(c) == 0:
        array.config(text=("Стоим..."))
    panel.config(image=img2)
    kef.config(text=str(f))
win = tk.Tk()
win.title('Elevator on python')
ph = tk.PhotoImage(file='') #closed elev
win.iconphoto(False, ph)
img = ImageTk.PhotoImage(Image.open(path))
img2 = ImageTk.PhotoImage(Image.open(path2))
ropes = tk.Label(win, height=30, bg='#000'); ropes.place(x=261, y=10)
panel = tk.Label(win, image = img); panel.place(x=x, y=245)
win.geometry("200x300+860+340")
win.minsize(300, 300); win.maxsize(300, 300)
win.config(bg='#808080') # fg; font; padx; width; height; anchor; font; text; relief; justify
btn1 = tk.Button(win, text='1', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn1), fg='#fff'); btn1.place(x=105, y=35)
btn2 = tk.Button(win, text='2', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn2), fg='#fff'); btn2.place(x=145, y=35)
btn3 = tk.Button(win, text='3', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn3), fg='#fff'); btn3.place(x=105, y=75)
btn4 = tk.Button(win, text='4', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn4), fg='#fff'); btn4.place(x=145, y=75)
btn5 = tk.Button(win, text='5', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn5), fg='#fff'); btn5.place(x=105, y=115)
btn6 = tk.Button(win, text='6', height=1, width=3, bg='#000', font=('bold arial', 12), command= lambda: Well(btn6), fg='#fff'); btn6.place(x=145, y=115)
start = tk.Button(win, text='lesss go', height=1, width=20, bg='#000', font=('bold arial', 12), command=Lesss_go, fg='#FFD700'); start.place(x=50, y=260)
placement = tk.Label(win, text=('Лифт находится на:\n' + '0' + ' этаже')); placement.place(x=90, y=180)
array = tk.Label(win, text=('Текущая очередь:\n' + ' '.join(c)), fg='#000'); array.place(x=90, y=220)
kef = tk.Button(win, text='245')
welc = tk.Label(win, text='''Warn Elevator''', width = 50, font='20')
welc.pack(pady=(10, 0))
win.mainloop()
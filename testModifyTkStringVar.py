import tkinter as tk

def click():
    # print(10+50)
    after = before.get()
    print(after)
    wrongEntry.delete(0,"end")
    wrongEntry.insert(0,"請輸入資料")
    print(revise_ID(after))

def revise_ID(after):
    ans = after.replace('~','-')
    ans = ans.replace('隻','-')
    ans = ans.replace('l','L')
    ans = ans.replace('d','D')
    ans = ans.replace('低','D')
    ans = ans.replace('第','D')
    ans = ans.replace('地','D')
    ans = ans.replace('y','Y')
    ans = ans.replace('外','Y')    
    ans = ans.replace('。','')
    return ans

win = tk.Tk()
win.title('hihi')

before = tk.StringVar()
after = tk.StringVar()
before.set(':)')
wrongEntry = tk.Entry(win, textvariable= before, fg='red')
wrongEntry.grid(column=0, row=0)
btn = tk.Button(win, text='push', command=click)
btn.grid(column=0, row=1)

win.mainloop()

# import tkinter as tk
# root = tk.Tk()
# root.title('my window')
# root.geometry('300x200')

# def button_event():
#     mybutton['text'] = 'hello wolrd'

# mybutton = tk.Button(root, text='button', command=button_event)
# mybutton.pack()

# root.mainloop()
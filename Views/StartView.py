from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import simpledialog as sd
import serial.tools.list_ports
from Utils.Logger import print


class StartView(tk.Frame):
    def __init__(self, parent, controller, system):
        tk.Frame.__init__(self, parent)
        self.controller, self.system = controller, system
        self.port = tk.StringVar()
        self.sampleSize = tk.IntVar()
        self.sampleSize.set(system.sampleSize)
        self.operateMode = tk.StringVar()
        self.operateMode.set("自動模式")
        self.recordMode = tk.StringVar()
        self.recordMode.set("窩重")
        self.fetchPorts()
        
        weightBtn = tk.Button(self, text="開始秤重", font=20,
                        command=lambda: [self.variableSetting(), self.checkPort()])
        advanceBtn = tk.Button(self, text="進階設定", font=20, command=self.advanceSetting)
        analyzeBtn = tk.Button(self, text="分析",
                        command=lambda: [self.variableSetting(), controller.show_frame("AnalyzeView", self.system)])
        weightBtn.pack(side=TOP,fill = X, padx=10, pady=5)
        advanceBtn.pack(side=TOP,fill = X, padx=10, pady=5)
        analyzeBtn.pack(side=TOP,fill = X, padx=10, pady=5)
        



    def fetchPorts(self):
        port_list = list(serial.tools.list_ports.comports())
        assert (len(port_list) != 0),"無可用串口"
        port_str_list = []
        for i in range(len(port_list)):
            lines = str(port_list[i])
            # print("port: " + str(i) + " " + str(port_list[i]))
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        self.port.set("請選擇連線串口埠")
        portCbb = ttk.Combobox(self, values=port_str_list, textvariable = self.port, state="readonly", width=15, font=20)
        portCbb.pack(side=TOP,fill = X, padx=10, pady=5)
    
    
    def variableSetting(self):
        self.system.port = self.port.get()
        self.system.sampleSize = self.sampleSize.get()
        self.system.operateMode = True if self.operateMode.get() == "自動模式" else False
        self.system.recordMode = True if self.recordMode.get() == "窩重" else False


    def thresholdSetting(self):
        temp = self.system.threshold  #default = 1
        user_input = sd.askfloat("設定儲存鎖定值", "請輸入儲存鎖定值")
        if user_input is not None:
            self.system.threshold = float(user_input)
        else:
            self.system.threshold = temp
    

    def advanceSetting(self):
        window = tk.Toplevel(self, bd=1, padx=3, pady=3)
        window.geometry("320x350")
        frame = ttk.LabelFrame(window,text="進階設定")
        frame.place(x=15,y=10)

        frame2 = ttk.LabelFrame(frame,text="記錄模式")
        frame2.pack()
        self.radio_btn1 = tk.Radiobutton(frame2, text="窩重＋母豬", font=20,variable=self.recordMode, value="窩重")
        self.radio_btn1.pack(side=LEFT,fill = X, padx=28, pady=5)
        self.radio_btn1.select()
        self.radio_btn2 = tk.Radiobutton(frame2, text="個別重", font=20,variable=self.recordMode, value="個別重")
        self.radio_btn2.pack(side=TOP,fill = X, padx=28, pady=5)

        frame3 = ttk.LabelFrame(frame,text="操作模式")
        frame3.pack()
        self.radio_btn3 = tk.Radiobutton(frame3, text="自動(超過鎖定值並平衡後數秒會紀錄)", font=20,variable=self.operateMode, value="自動模式")
        self.radio_btn3.pack(side=TOP,fill = X, padx=10, pady=5)
        self.radio_btn3.select()
        self.radio_btn4 = tk.Radiobutton(frame3, text="手動", font=20,variable=self.operateMode, value="手動模式")
        self.radio_btn4.pack(side=TOP,fill = X, padx=10, pady=5)
        
        tk.Label(frame,text="取樣數", font=7).pack(side=TOP, padx=10, pady=5, anchor=tk.W)
        sample_size = ttk.Combobox(frame,values=[30, 40, 50], textvariable = self.sampleSize, state="readonly", width=12, font=10)
        sample_size.pack(side=TOP, fill = X, padx=10, pady=5)

        thresholdBtn = tk.Button(frame,text="設定儲存鎖定值",  command=self.thresholdSetting, font=12)
        thresholdBtn.pack(side=TOP, fill = X, padx=10, pady=5)

        """#testMode
        testModeBtn = tk.Button(frame,text="test",  command=self.testMode, font=12)
        testModeBtn.pack(side=TOP, fill = X, padx=10, pady=5)"""


    def checkPort(self):
        try:  # open and connect port  
            self.system.serialthread.open_port(self.system.port)
        except:
            tk.messagebox.showwarning(title="錯誤", message='請選擇正確串口埠')
            return
        self.controller.show_frame("ScaleView", self.system)



    def testMode(self):
        print(self.operateMode.get())
        print(self.recordMode.get())
        self.system.operateMode = True if self.operateMode.get() == "自動模式" else False
        self.system.recordMode = True if self.recordMode.get() == "窩重" else False
        print(self.system.operateMode)
        print(self.system.recordMode)

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
        self.stage_var = tk.StringVar()
        self.stage_var.set("三周齡")
        self.mode_var = tk.StringVar()
        self.mode_var.set("自動模式")
        self.num_var = tk.StringVar()
        self.num_var.set("累加模式")
        self.modeValue = tk.StringVar()
        self.numValue = tk.StringVar()

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

        self.system.autoMode = True if self.mode_var.get() == "自動模式" else False
        self.system.numMode = True if self.num_var.get() == "累加模式" else False


    def thresholdSetting(self):
        temp = self.system.threshold
        user_input = sd.askfloat("設定儲存鎖定值", "請輸入儲存鎖定值")
        if user_input is not None:
            self.system.threshold = float(user_input)
        else:
            self.system.threshold = temp
    

    def advanceSetting(self):
        window = tk.Toplevel(self, bd=1, padx=3, pady=3)
        window.geometry("230x320")
        frame = ttk.LabelFrame(window,text="進階設定")
        frame.place(x=15,y=10)

        frame2 = ttk.LabelFrame(frame,text="豬隻階段設定")
        frame2.pack()
        self.stage_mode = tk.Button(frame2, text="三周齡/離乳", font=20, command=self.weaningStageSetting)
        self.stage_mode.pack(side=TOP,fill = X, padx=10, pady=5)
        self.stage_mode = tk.Button(frame2, text="保育", font=20, command=self.nurseryStageSetting)
        self.stage_mode.pack(side=TOP,fill = X, padx=10, pady=5)
        self.stage_mode = tk.Button(frame2, text="生長/肥育", font=20, command=self.growwingStageSetting)
        self.stage_mode.pack(side=TOP,fill = X, padx=10, pady=5)
        
        tk.Label(frame,text="取樣數", font=7).pack(side=TOP, padx=10, pady=5, anchor=tk.W)
        sample_size = ttk.Combobox(frame,values=[30, 40, 50], textvariable = self.sampleSize, state="readonly", width=12, font=10)
        sample_size.pack(side=TOP, fill = X, padx=10, pady=5)


    def weaningStageSetting(self):
        window = tk.Toplevel(self, bd=1, padx=3, pady=3)
        window.geometry("230x300")
        thresholdBtn = tk.Button(window,text="設定儲存鎖定值",  command=self.thresholdSetting, font=12)
        thresholdBtn.pack(side=TOP, fill = X, padx=10, pady=5)
        self.riobtn1 = tk.Radiobutton(window, text="自動批次模式" , variable=self.modeValue, value="自動模式", font=10)
        self.riobtn1.pack(side=TOP,fill = X, padx=10, pady=5)
        self.riobtn2 = tk.Radiobutton(window, text="手動批次模式" , variable=self.modeValue, value="手動模式", font=10)
        self.riobtn2.pack(side=TOP,fill = X, padx=10, pady=5)
        self.riobtn3 = tk.Radiobutton(window, text="手動窩重模式" , variable=self.modeValue, value="新設定", font=10)
        self.riobtn3.pack(side=TOP,fill = X, padx=10, pady=5)
        self.riobtn1.select()
        if(self.modeValue=="新設定"):
            self.mode_var.set("手動模式")
            self.num_var.set("單次模式")
        self.mode_var.set(self.modeValue.get())
        
        

    def nurseryStageSetting(self):
        window = tk.Toplevel(self, bd=1, padx=3, pady=3)
        window.geometry("230x300")
        self.riobtn4 = tk.Radiobutton(window, text="手動單次模式" , variable=self.numValue, value="單次模式", font=10)
        self.riobtn4.pack(side=TOP,fill = X, padx=10, pady=5)
        self.riobtn5 = tk.Radiobutton(window, text="手動批次模式" , variable=self.numValue, value="累加模式", font=10)
        self.riobtn5.pack(side=TOP,fill = X, padx=10, pady=5)
        self.mode_var.set("手動模式")
        self.riobtn4.select()
        self.num_var.set(self.numValue.get())

        
    
    def growwingStageSetting(self):
        window = tk.Toplevel(self, bd=1, padx=3, pady=3)
        window.geometry("230x300")

        self.riobtn6 = tk.Radiobutton(window, text="手動單次模式" , variable=self.numValue, value="單次模式", font=10)
        self.riobtn6.pack(side=TOP,fill = X, padx=10, pady=5)
        self.mode_var.set("手動模式")
        self.num_var.set(self.numValue.get())


    def checkPort(self):
        try:  # open and connect port  
            self.system.serialthread.open_port(self.system.port)
        except:
            tk.messagebox.showwarning(title="錯誤", message='請選擇正確串口埠')
            return
        self.controller.show_frame("ScaleView", self.system)
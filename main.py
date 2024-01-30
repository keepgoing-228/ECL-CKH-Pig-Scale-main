# if getattr(sys, 'frozen', False):
#       #覆盖dll搜索路径。
#   ctypes.windll.kernel32.SetDllDirectoryW('D:/Users/ASUS/anaconda3/Library/bin')
#   # 加载外部dll的初始化代码
#   ctypes.CDLL('libiomp5md.dll')
#   ctypes.CDLL('mkl_core.dll')
#   ctypes.CDLL('mkl_intel_thread.dll')
#   # ctypes.CDLL('mkl_p4.dll')
#   # 恢复dil搜索路径。
#   ctypes.windll.kernel32.SetDllDirectoryW(sys._MEIPASS)

from Views.GUI import GUI
from Structure.DataStructure import Scale


system = Scale()
view = GUI(system)
view.mainloop()

import os
import ctypes
import sys
 


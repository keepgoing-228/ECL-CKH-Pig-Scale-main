import serial  # 引用pySerial模組
 
COM_PORT = 'COM1'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率

ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

try:
    for i in range(500):
        ser.write(b"ST,GS,+  0.00 kg\n")
    for i in range(500):
        ser.write(b"ST,GS,+  2.00 kg\n")
    for i in range(500):
        ser.write(b"ST,GS,+  5.10 kg\n")
    for i in range(500):
        ser.write(b"ST,GS,+  9.15 kg\n")
    while True:
        ser.write(b"ST,GS,+  0.00 kg\n")

        
 
except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('bye!!')
import serial
import serial.tools.list_ports
import re

ports = serial.tools.list_ports.comports()
pname, pid = {}, {}
for n, (port, desc, hwid) in enumerate(sorted(ports)):
        print("{}: {} [{}]".format(port, desc, hwid))
        pname[n] = port
        pid[n] = hwid

pattern1 = re.compile("\d.\d*") 
pattern2 = re.compile("PID=(\d*):\d\d\d\d")

for i in range(len(ports)):
    if re.findall(pattern2, pid[i])[0] == '1A86': # Change '1A86' to the Arduino port  id. 
        print('here')
        ser1=serial.Serial(pname[i],9600,timeout=1)# arduino   
    else:    
        ser2=serial.Serial(pname[i],9600,timeout=1)# weighing scale

while True: # Run forever
    read_ser2=ser2.read_until(b'S')
    weight=re.search(pattern1 , read_ser2.decode()).group()
    if (weight != ""):
        print('weight is ', weight)
        if float(weight) < 1.3:
            ser1.write(b'ON\n')
            print('arduino input ON')
        else:
            ser1.write(b'OFF\n')
            print('arduino input OFF')


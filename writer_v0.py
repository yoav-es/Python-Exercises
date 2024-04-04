from pymodbus.client import ModbusSerialClient as mbRtuObj
from pymodbus.client import ModbusTcpClient as mbTcpObj
from pymodbus.exceptions import ModbusException
from time import sleep
#CONSTANTS
REG_TO_READ = 0
REG_TO_WRITE = 0
PORT_RTU = 'COMX' # COM FOR WINDOWS, 
#PORT_RTU = 'dev/serial/by-id/usb-1a86_USB_Serial-if00-port0' #port for linux(ubuntu)
BAUD = 0
UID  = 0
VALUE = 0
#using ethernet port 
ADDR = '127.0.0.1'
PORT_TCP = 502
#Modbus RTU Function
with mbRtuObj(port = PORT_RTU, baudrate = BAUD) as client:
    try:
        #writing
        client.write_register(REG_TO_WRITE,VALUE,unit = UID)
        print(f'wrote {VALUE} to {UID} in reg {REG_TO_WRITE}')
    except ModbusException as err:
        print(f'{err} occured')

#Modbus TCP version
with mbTcpObj(host= ADDR,port = PORT_TCP) as client:
    try:
        #writing
        client.write_register(REG_TO_WRITE,VALUE,unit = UID)
        print(f' wrote {VALUE} to {UID} in reg {REG_TO_WRITE}')
    except ModbusException as err:
        print(f'{err} occured')
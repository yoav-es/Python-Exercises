from pymodbus.client import ModbusSerialClient as mbRtuObj
from pymodbus.client import ModbusTcpClient as mbTcpObj
from pymodbus.exceptions import ModbusException
import sys 
#CONSTANTS


#base assumptions - connection method, port, and baudrate or tcp address are known 
PORT_RTU = 'COMX' # COM FOR WINDOWS, 
# PORT_RTU = 'dev/serial/by-id/usb-1a86_USB_Serial-if00-port0' #port for linux(ubuntu)
# PORT_RTU = 'dev/ttyO3'
BAUD = 9600

#using ethernet port 
ADDR = '127.0.0.1'
PORT_TCP = 502
#Modbus RTU Function
def func():
    if len(sys.argv) != 5:
        print("arguments missing")
        sys.exit()
    UID          = sys.argv[1]
    VALUE        = sys.argv[2]
    REG_TO_WRITE = sys.argv[3]
    MODE         = sys.argv[4]
    #using modbus rtu
    try:
        while True:
            if MODE == 'R':
                with mbRtuObj(port = PORT_RTU, baudrate = BAUD) as client:
                    try:
                        #writing
                        client.write_register(REG_TO_WRITE,VALUE,unit = UID)
                        print(f'wrote {VALUE} to {UID} in reg {REG_TO_WRITE}')
                    except ModbusException as err:
                        print(f'{err} occured')
            #using modbus tcp 
            elif MODE == "T": 
            #Modbus TCP version
                with mbTcpObj(host= ADDR,port = PORT_TCP) as client:
                    try:
                        #writing
                        client.write_register(REG_TO_WRITE,VALUE,unit = UID)
                        print(f' wrote {VALUE} to {UID} in reg {REG_TO_WRITE}')
                    except ModbusException as err:
                        print(f'{err} occured')
            else:
                print("re-enter arguments or 'q' to quit")
                UID          = input("enter UID ")
                VALUE        = input("enter VALUE ")
                REG_TO_WRITE = input("enter REG_TO_WRITE ")
                MODE         = input("enter MODE ")
                print(f"selected parameters - UNIT ID = {UID}, Value = {VALUE}, REGISTER = {REG_TO_WRITE} protocl method = {MODE}")
                print("enter y to confirm or n to change parameter")

    except KeyboardInterrupt:
        print("exiting")
        sys.exit()

if __name__ == "__main__":
    print((sys.argv))
    func()
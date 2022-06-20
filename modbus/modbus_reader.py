from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import csv
from datetime import datetime
from time import sleep


#default values
BAUD = 9600
PORT = 'COM6'
METHOD = 'rtu'
T_OUT = 1
STOPBIT = 2
BYTESIZE = 8
PARITY = 'N'
ADDRESS = [108,116,119]
COUNT = 1 #4 read output,8 read registers
UNIT = 2 # slave device address



# a function to write sensor data into a csv file.
def writeData(data):
    with open('sensor_output.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= ['time_stamp', 'sensor_reading'])
        writer.writeheader()
        writer.writerows(data)


# A function that reads the sensor output and writes it to a file.
def getmeasure():
    client = ModbusClient(method=METHOD, port=PORT, baudrate=BAUD, parity=PARITY)
    data = {}
    while client.connect():
        #1st try
        read1 = client.read_holding_registers(address= ADDRESS[0], count=COUNT, unit=UNIT)
        read2 = client.read_holding_registers(address= ADDRESS[1], count=COUNT, unit=UNIT)
        read3 = client.read_holding_registers(address= ADDRESS[2], count=COUNT, unit=UNIT)


        print(read1.registers)
        print(read2.registers)
        print(read3.registers)

        sleep(1)
        dt = datetime.now()
        ts = datetime.timestamp(dt)

    client.close()
    writeData(data)


def main():
    getmeasure()


if __name__ == "__main__":
    main()


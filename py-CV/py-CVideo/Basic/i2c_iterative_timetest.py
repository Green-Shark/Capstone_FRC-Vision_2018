import smbus2
import numpy as np
import time
import random

rpi_bus = smbus2.SMBus(1)
rpi_wrapper = smbus2.SMBusWrapper(1)



slave_add = 0x04

def send_w_wrapper(number):
    with smbus2.SMBusWrapper(1) as bus:
        bus.write_i2c_block_data(slave_add, 0, number)

def send_regular(number):
    rpi_bus.write_byte(slave_add, number)


def main():

    list_1 = []

    ##Receives the data from the User
    #data = raw_input("Enter the data to be sent : ")
    #data_list = list(data)
    #for i in data_list:
    #	#Sends to the Slaves 
    #    writeNumber(int(ord(i)))
    #    time.sleep(.1)

    for x in range(0, 10):
        num = random.randint(1, 9999)
        list_1.append(num)
    
    for y in range(0, 10):
        number = list_1[y]
        print(number)
        send_regular(int(ord(number)))
        time.sleep(.2)


if __name__ == '__main__':
    main()
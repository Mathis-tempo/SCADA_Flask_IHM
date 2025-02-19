#! /bin/python

###########
# IMPORTS #
###########

from pyModbusTCP.client import ModbusClient
from time import sleep

#############
# VARIABLES #
#############

slaveAddress='127.0.0.1'
slavePort=502
EntryConveyor=0   
ExitConveyor=2
StopBlade=1
SorterBelt1=4
SorterBelt2=6
SorterBelt3=8


SorterTurn1=3
SorterTurn2=5
SorterTurn3=7

VisionSensor=0x00


counter1=0x00
counter2=0x01
counter3=0x02


########
# CODE #
########
def run():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()


    #INIT SETUP
    
    client.write_single_coil(EntryConveyor,1)
    client.write_single_coil(ExitConveyor,1)
    client.write_single_coil(StopBlade,0)

    client.write_single_coil(SorterBelt1,1)
    client.write_single_coil(SorterBelt2,1)
    client.write_single_coil(SorterBelt3,1)
                    
    client.write_single_coil(SorterTurn1,0)
    client.write_single_coil(SorterTurn2,0)
    client.write_single_coil(SorterTurn3,1)

    client.write_single_coil(counter1, 1) 
    client.write_single_coil(counter2, 1) 
    client.write_single_coil(counter3, 1)

    count1=0
    count2=0
    count3=0
    client.write_single_register(counter1, count1)              
    client.write_single_register(counter2, count2)              
    client.write_single_register(counter3, count3)              
    
    #DRIVER LOGIC

    try:
        while True:
            sensor_value = client.read_input_registers(VisionSensor, 1)

            if sensor_value:
        
                color = sensor_value[0]            

                if color == 1 or color == 2 or color == 3:
                    count1= count1 +1                
                    client.write_single_register(counter1, count1)              
                    sleep(1)
                    client.write_single_coil(EntryConveyor,0)
                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)
                    client.write_single_coil(SorterTurn1,1)
                    sleep(1)
                    client.write_single_coil(SorterTurn1,0)
                    
                if color == 4 or color == 5 or color == 6:
                    count2 = count2 +1      
                    client.write_single_register(counter2, count2)                              
                    sleep(1)
                    client.write_single_coil(EntryConveyor,0)
                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)                
                    client.write_single_coil(SorterTurn2,1)
                    sleep(4)
                    client.write_single_coil(SorterTurn2,0)

                if color == 7 or color == 8 or color == 9: 
                    count3 = count3 + 1      
                    client.write_single_register(counter3, count3)                              
                    sleep(1)
                    client.write_single_coil(EntryConveyor,0)
                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)                
                    sleep(6)
                    client.write_single_coil(SorterTurn2,0)

                client.write_single_coil(StopBlade,0)
                client.write_single_coil(EntryConveyor,1)
            
    except KeyboardInterrupt:
        print("exiting")
        client.write_single_coil(EntryConveyor, 0)
        client.write_single_coil(ExitConveyor, 0)
        client.close()


#FLASK LOGIC

def start_entry_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(EntryConveyor, 1)
    client.close()

def stop_entry_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(EntryConveyor, 0)
    client.close()

def start_exit_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(ExitConveyor, 1)
    client.close()

def stop_exit_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(ExitConveyor, 0)
    client.close()

def start_sorter1():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(SorterTurn1, 1)
    client.close()

def stop_sorter1():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    client.write_single_coil(SorterTurn1, 0)
    client.close()



if __name__ == "__main__":
    run()


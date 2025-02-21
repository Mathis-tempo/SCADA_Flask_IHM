#! /bin/python

###########
# IMPORTS #
###########

from pyModbusTCP.client import ModbusClient
from time import sleep
from state import system_state  

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
    client.write_single_coil(EntryConveyor, 1)
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
    
    system_state.entry_conveyor_state = True
    system_state.exit_conveyor_state = True
    system_state.sorter1_state = False
    system_state.sorter2_state = False
    system_state.sorter3_state = True           
    
    #MAIN DRIVER LOGIC

    try:
        while True:
            sensor_value = client.read_input_registers(VisionSensor, 1)

            if sensor_value:
        
                color = sensor_value[0]

                if color in [1, 2, 3]:
                    count1= count1 +1                
                    client.write_single_register(counter1, count1)              
                    sleep(1)
                    if not system_state.entry_controlled_by_flask:
                        client.write_single_coil(EntryConveyor,0)
                        system_state.entry_conveyor_state = False  
                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)
                    if not system_state.sorter1_controlled_by_flask:
                        client.write_single_coil(SorterTurn1,1)
                        system_state.sorter1_state = True  

                    sleep(1)
                    if not system_state.sorter1_controlled_by_flask:
                        client.write_single_coil(SorterTurn1,0)
                        system_state.sorter1_state = False 
                    
                if color in [4, 5, 6]:
                    count2 = count2 +1      
                    client.write_single_register(counter2, count2)                              
                    sleep(1)
                    if not system_state.entry_controlled_by_flask:
                        client.write_single_coil(EntryConveyor,0)
                        system_state.entry_conveyor_state = False 

                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)   
                    if not system_state.sorter2_controlled_by_flask:
                        client.write_single_coil(SorterTurn2,1)
                        system_state.sorter2_state = True 

                    sleep(4)
                    if not system_state.sorter2_controlled_by_flask:
                        client.write_single_coil(SorterTurn2,0)
                        system_state.sorter2_state = False 


                if color in [7, 8, 9]:
                    count3 = count3 + 1      
                    client.write_single_register(counter3, count3)                              
                    sleep(1)
                    if not system_state.entry_controlled_by_flask:
                        client.write_single_coil(EntryConveyor,0)
                        system_state.entry_conveyor_state = False 

                    sleep(0.2)
                    client.write_single_coil(StopBlade,1)                
                    sleep(6)


                client.write_single_coil(StopBlade,0)
                
                if not system_state.entry_controlled_by_flask:
                    client.write_single_coil(EntryConveyor,1)
                    system_state.entry_conveyor_state = True 
                if not system_state.exit_controlled_by_flask:
                    client.write_single_coil(ExitConveyor,1) 
                    system_state.exit_conveyor_state = True 
                if not system_state.sorter3_controlled_by_flask:
                    client.write_single_coil(SorterTurn3,1)
                    system_state.sorter3_state = True 


            
    except KeyboardInterrupt:
        print("exiting")
        client.write_single_coil(EntryConveyor, 0)
        client.write_single_coil(ExitConveyor, 0)
        client.close()


#FLASK LOGIC

def toggle_entry_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    current_state = client.read_coils(EntryConveyor, 1)[0]
    client.write_single_coil(EntryConveyor, not current_state)
    system_state.entry_conveyor_state = not current_state
    client.close()


def toggle_exit_conveyor():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    current_state = client.read_coils(ExitConveyor, 1)[0]
    client.write_single_coil(ExitConveyor, not current_state)
    system_state.exit_conveyor_state = not current_state
    client.close()

def toggle_sorter1():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    current_state = client.read_coils(SorterTurn1, 1)[0]
    client.write_single_coil(SorterTurn1, not current_state)
    system_state.sorter1_state = not current_state
    client.close()

def toggle_sorter2():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    current_state = client.read_coils(SorterTurn2, 1)[0]
    client.write_single_coil(SorterTurn2, not current_state)
    system_state.sorter2_state = not current_state
    client.close()

def toggle_sorter3():
    client = ModbusClient(slaveAddress,port=slavePort,unit_id=1)
    client.open()
    current_state = client.read_coils(SorterTurn3, 1)[0]
    client.write_single_coil(SorterTurn3, not current_state)
    system_state.sorter3_state = not current_state
    client.close()

if __name__ == "__main__":
    run()


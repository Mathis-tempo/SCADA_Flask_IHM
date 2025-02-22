class ConveyorState:
    def __init__(self):
        self.entry_conveyor_state = True
        self.exit_conveyor_state = True
        self.sorter1_state = False
        self.sorter2_state= False
        self.sorter3_state= False

        self.entry_controlled_by_flask = False
        self.exit_controlled_by_flask = False
        self.sorter1_controlled_by_flask = False    
        self.sorter2_controlled_by_flask = False    
        self.sorter3_controlled_by_flask = False  

        self.BlueCounter=0
        self.GreenCounter=0
        self.MetalCounter=0  

system_state = ConveyorState()
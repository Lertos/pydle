from enum import Enum


class State(Enum):
    MAIN_MENU = 'mainMenu'
    CITY = 'city'
    SHOP = 'shop'
    OPTIONS = 'options'
    TRAVEL = 'travel'
    

class StateHandler:
    
    def __init__(self, gameData, characterPanel, mainPanel, chatPanel):
        self.gameData = gameData
        
        self.characterPanel = characterPanel
        self.mainPanel = mainPanel
        self.chatPanel = chatPanel
        
        self.currentState = State.MAIN_MENU
        self.currentOptions = []
        
        self.processMainMenu()

        print(self.gameData.getCity('varrock'))
        

    def handleKeyCommand(self, key):
        print(key)
        if self.currentState == State.MAIN_MENU:
            self.processMainMenu(key)
        pass
    
    
    def addOption(self, state, displayText):
        return {
            'state': state,
            'displayText': displayText,
            'previousState': self.currentState
        }
    
    
    def convertOptionsToText(self, text):
        for i in range(len(self.currentOptions)):
            text.append('yellow::' + str(i+1) + ': ::white::' + self.currentOptions[i]['displayText'] + '::')
    
    
    def setMainPanelText(self):
        text = []
        text.append(self.mainText)
        text.append('\n::')
        
        self.convertOptionsToText(text)
        
        self.mainPanel.setTextToDraw(text)
            
    
    #TODO - have all different types of screens; travel, combat, shops, etc; look at doc list
    def processMainMenu(self, key='-1'):
        options = []
        
        if key == '-1':
            self.mainText = 'red::Explore the world of Noxphor::\n::'

            options.append(self.addOption(State.CITY, 'Start Game'))
            options.append(self.addOption(State.OPTIONS, 'Options'))
        elif key == '1':
            self.mainText = 'red::Testing a key press::\n::'

        self.currentOptions = options
        self.setMainPanelText()
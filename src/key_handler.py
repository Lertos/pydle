
class KeyHandler:
    
    def __init__(self, pygame):
        self.pygame = pygame
        self.currentKeys = []
        
        self.singleKeyMode = True #For single key commands
        self.clearKeysNextFrame = False #Queues the current key list to be deleted at the end of next frame 
        
        
    def addPressedKey(self, pressedKey):
        if self.singleKeyMode:
            self.clearKeys()
            
        key = self.getKeyFromKeyCode(pressedKey)
        
        if key != -1:
            self.currentKeys.append(key)
    
    
    def startSingleKeyMode(self):
        self.clearKeys()
        self.singleKeyMode = True
        print('SINGLE MODE activated')
        
        
    def startMultiKeyMode(self):
        self.clearKeys()
        self.singleKeyMode = False
        print('MULTI MODE activated')
        
        
    def getAllKeys(self):
        return ''.join(self.currentKeys)
    
    
    def clearKeys(self):
        self.currentKeys = []
    

    def removeCharacter(self):
        if len(self.currentKeys) > 0:
            self.currentKeys.pop()

        
    def getKeyFromKeyCode(self, key):
        try:
            return chr(key)
        except:
            return -1
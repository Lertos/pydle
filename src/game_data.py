    
class GameData():  
    
    def getCity(self, cityKey):
        return gameData[cityKey]


gameData = {
    'varrock': {
        'cityInfo': 'A great place with a fountain',
        'position': '123,32', #position will determine where on the map it should be related to others
        'npcs': [
            'sally_verdun',
            'jordan_noka'
        ],
        'skill_nodes': {
            'woodcutting': {
                'oak': {
                    'maxLogsPerDay': 0
                }
            }
        }
    }
}
import requests
import random as r
import set_board

create_card_endpoint = "https://api.trello.com/1/cards"
words = ["Lynx", "Eridanus", "Cassiopeia", "Scorpius", "Crux", "Cancer", "Leo", "Canis Major", "Andromeda", "Taurus", "Sagittarius", "Lyra", "Serpens", "Aquarius", "Cygnus", "Corvus", "Ursa Major", "Cepheus"]

class Card:
    def __init__(self):
        self.idBoard = set_board.idBoard

    def create_trello_card(self):
        pass    

class Issue(Card):
    def __init__(self,title,description):
        Card.__init__(self)
        self.title = title
        self.description = description
        self.idList = set_board.listIdDict["To Do"]

    def create_trello_card(self):
        jsonObj = {"key" : set_board.API_KEY, "token" : set_board.API_TOKEN, "idList" : self.idList, "name" : self.title, "desc" : self.description}
        new_card = requests.post(create_card_endpoint, json = jsonObj)

class Bug(Card):
    def __init__(self,description):
        Card.__init__(self)
        self.description = description
        self.idList = set_board.listIdDict["Bugs"]
        self.idLabel = set_board.labelIdDict["Bug"]
        self.idMember = set_board.membersIdList[r.randint(0,len(set_board.membersIdList) -1 )]
        self.cardName = "bug-" + words[r.randint(0,len(words) -1)] + "-" + str(r.randint(0,500))
        print(self.idMember)

    def create_trello_card(self):
        jsonObj = {"key" : set_board.API_KEY, "token" : set_board.API_TOKEN, "idList" : self.idList, "name" : self.cardName, "desc" : self.description, "idMembers" : [self.idMember], "idLabels" : [self.idLabel]}
        new_card = requests.post(create_card_endpoint, json = jsonObj)

class Task(Card):
    def __init__(self,title,category):
        Card.__init__(self)
        self.title = title
        self.idList = set_board.listIdDict["Tasks"]
        self.idLabel = set_board.labelIdDict[category]

    def create_trello_card(self):
        jsonObj = {"key":set_board.API_KEY, "token":set_board.API_TOKEN, "idList" : self.idList, "name" : self.title, "idLabels" : [self.idLabel]}
        new_card = requests.post(create_card_endpoint, json = jsonObj)


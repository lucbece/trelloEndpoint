import requests
import random as r

#Replace API_TOKEN with the authtoken you've generated
API_KEY = "a3d9b7ff12d04573f01ec9dd451ed03f"
API_TOKEN = "YOUR TOKEN GOES HERE"


def create_board(boardName,API_KEY,API_TOKEN):
    create_board_endpoint = "https://api.trello.com/1/boards/"
    jsonObj = {"key":API_KEY, "token":API_TOKEN,"name":boardName}
    req = requests.post(create_board_endpoint, json = jsonObj)

def get_board_id(boardname,API_KEY,API_TOKEN):
    get_boards_endpoint = f"https://api.trello.com/1/members/me/boards?key={API_KEY}&token={API_TOKEN}"
    request = requests.get(get_boards_endpoint)
    boardsJson = request.json()
    for board in boardsJson:
        if (board["name"] == boardname):
            return board["id"]
    return "-1"

def create_list(listName, boardId, API_KEY, API_TOKEN):
    create_list_endpoint = f'https://api.trello.com/1/lists?name={listName}&idBoard={boardId}'
    authJson = {"key" : API_KEY, "token" : API_TOKEN}
    request = requests.post(create_list_endpoint, json = authJson)            

def get_list_id(listName, boardId, API_KEY, API_TOKEN):
    get_list_endpoint = f"https://api.trello.com/1/boards/{boardId}/lists"
    request = requests.get(get_list_endpoint, json = {"key":API_KEY, "token":API_TOKEN})
    jsonArr = request.json()
    for list in jsonArr:
        if(list["name"] == listName):
            return list["id"]
    return "-1"        
        

def create_label(idBoard, labelName, API_KEY, API_TOKEN):
    colors = ["yellow", "purple", "blue", "red", "green", "orange", "black", "sky", "pink", "lime"]
    jsonObj = {"key" : API_KEY, "token" : API_TOKEN}
    create_label_endpoint = f"https://api.trello.com/1/labels?name={labelName}&color={colors[r.randint(0,len(colors)-1)]}&idBoard={idBoard}"
    req = requests.post(create_label_endpoint, json = jsonObj)

        
def get_label_id(idBoard, labelName, API_KEY, API_TOKEN):
    jsonObj = {"key" : API_KEY, "token" : API_TOKEN}
    get_label_endpoint = f"https://api.trello.com/1/boards/{idBoard}/labels"
    req = requests.get(get_label_endpoint, json = jsonObj)
    reqJson = req.json()
    for label in reqJson:
        if(label['name'] == labelName):
            return label["id"]
    return "-1"

def get_members_id(idBoard,API_KEY,API_TOKEN):
    get_members_endpoint = f"https://api.trello.com/1/boards/{idBoard}/memberships"
    jsonObj = jsonObj = {"key" : API_KEY, "token" : API_TOKEN, "filter" : "normal"}
    req = requests.get(get_members_endpoint, json = jsonObj)
    membersArr = req.json()
    idList = []
    for member in membersArr:
        idList.append(member["idMember"])
    return idList



#---------------------------------------------------------------------------------------------------------#

#First it checks wether the "Developer Team" board exists. If it doesn't, it must create it.
idBoard = get_board_id("Developer Team", API_KEY,API_TOKEN)
if idBoard == "-1":
    create_board("Developer Team", API_KEY, API_TOKEN)
    idBoard = get_board_id("Developer Team", API_KEY, API_TOKEN)

#It repeats the same process, this time with the lists in which the tickets will be placed.
listList = ["To Do", "Bugs", "Tasks"]
listIdDict = {}
for L in listList:
    tempListId = get_list_id(L, idBoard, API_KEY, API_TOKEN)
    if tempListId == "-1":
        create_list(L, idBoard, API_KEY, API_TOKEN)
        tempListId = get_list_id(L, idBoard, API_KEY, API_TOKEN)
    listIdDict[L] = tempListId
  

#Create a dictionary for labels and their iDs
labelList = ["Bug", "Maintenance", "Research", "Test"]
labelIdDict = {}
for label in labelList:
    tempLabelId = get_label_id(idBoard, label, API_KEY, API_TOKEN)
    if tempLabelId == "-1":
        create_label(idBoard, label, API_KEY, API_TOKEN)
        tempLabelId = get_label_id(idBoard, label, API_KEY, API_TOKEN)
    labelIdDict[label] = tempLabelId        

membersIdList = get_members_id(idBoard, API_KEY, API_TOKEN)
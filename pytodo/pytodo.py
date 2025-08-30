import os
import shutil

def getBaseDirectory():
    return os.path.dirname(__file__)

def getListsFolderLocation():
    lists_dir = os.path.join(getBaseDirectory(), "lists")
    return lists_dir

def getArchiveFolderLocation():
    archive_dir = os.path.join(getBaseDirectory(), "archive")
    return archive_dir

def makeList(lists_dir):
    print("Input name of new list:")
    listName = input()
    with open(os.path.join(lists_dir, f"{listName}.txt"), "w") as f:
        f.write("")
        print(listName + " created")
        f.close()
    return

def selectList():
    displayLists()
    print("\nType List Name to Load:\n")
    selectedList = input()
    if checkTaskListExists(selectedList):
        print(f"{selectedList} loaded: ")
        return
    else:
        print(f"list not found")
    return

def deleteList():
    print("Select list to delete")
    return

def startUpChecks():
    base_dir = os.path.dirname(__file__)  # folder where pytodo.py is
    lists_dir = os.path.join(base_dir, "lists")
    os.makedirs(lists_dir, exist_ok=True)  # create folder if missing
    return lists_dir

def displayLists():
    list = os.listdir("lists")
    for i in list:
        if (i[-4:]) == ".txt":
            print(i[:-4] + "\n")
    return

def checkForFile(fileLocation):
    return os.path.exists(fileLocation) and os.path.isfile(fileLocation)

def checkTaskListExists(taskName):
    fileLocation = getListsFolderLocation() + "/" + taskName + ".txt"
    return checkForFile(fileLocation)

def archiveList():
    print("\nSelect list to archive: \n")
    displayLists()
    listToArchive = input()
    if(checkTaskListExists(listToArchive)):
        print(f"\nList \"{listToArchive}\" located and moved to archived lists.")
        shutil.move(f"{fileLocation}", f"{getArchiveFolderLocation()}/{listToArchive}.txt")
    else:
        print(f"\nList \"{listToArchive}\" selected not located. Please try again")
    return

def readList(fileLocation):
    with open(os.path.join(lists_dir, f"{listName}.txt"), "r") as f:
        for x in f:
            print(x)
    f.close()
    return


def main():
    lists_dir = startUpChecks()
    print("  ____       _____     ____        \n |  _ \\ _   |_   _|__ |  _ \\  ___  \n | |_) | | | || |/ _ \\| | | |/ _ \\ \n |  __/| |_| || | (_) | |_| | (_) |\n |_|    \\__, ||_|\\___/|____/ \\___/ \n        |___/                      ")
    print("--------------------------------------------\n\n")
    exitBool = False
    while(not exitBool):
        print("1. Make List")
        print("2. Select List")
        print("3. Delete List")
        print("4. Archive List")
        print("9. Exit Application")
        choice = int(input())
        match choice:
            case 1:
                makeList(lists_dir)
            case 2:
                selectList()
            case 3:
                deleteList()   
            case 4:
                archiveList()
            case 9:
                exitBool = True
    

class list:
    def __init__(self, tasks):
        tasks = []
        
    def __str__(self):
        return f"{self.tasks}"

    def addTask():
        tasks.append(objective())
    
    def listTasks():
        taskNum = 0
        for task in tasks:
            print(f"{taskNum}: {task.task} ")
            if task.finished == true:
                print("✓")
            else:
                print("x")
                
    def readTasks():
        return

    def writeTasks():
        return
        


    

class objective:
    def __init__(self, task, finished):
        self.task = task
        self.finished = False
    
    def __str__(self):
        return f"{self.task} is finished: {self.finished}"

if __name__ == "__main__":
    main()



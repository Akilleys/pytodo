import os

def makeList(lists_dir):
    print("Input name of new list:")
    listName = input()
    with open(os.path.join(lists_dir, f"{listName}.txt"), "w") as f:
        f.write("")
        print(listName + " created")
        f.close()
    return

def selectList(listName):
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
    print("\nYour lists: \n")
    list = os.listdir("lists")
    for i in list:
        print(i[:-4] + "\n")
    return

def archiveList():
    return

def main():
    lists_dir = startUpChecks()
    print("  ____       _____     ____        \n |  _ \\ _   |_   _|__ |  _ \\  ___  \n | |_) | | | || |/ _ \\| | | |/ _ \\ \n |  __/| |_| || | (_) | |_| | (_) |\n |_|    \\__, ||_|\\___/|____/ \\___/ \n        |___/                      ")
    print("--------------------------------------------")
    print("1. Make List")
    print("2. Select List")
    print("3. Delete List")
    print("4. Archive List")
    choice = int(input())
    match choice:
        case 1:
            makeList(lists_dir)
        case 2:
            displayLists()
        case 3:
            deleteList()
        case 4:
            archiveList()

class list:
  def __init__(self, name, age):
    self.name = name
    self.age = age

if __name__ == "__main__":
    main()



import json

"""
    user to be able to write note, enter topic, lecture and content
    |
    this note will then be save to an external json file
    |
    user will be able to check note and also delete certain note that are no longer usful
    |
    view note function not available for now
"""
print("Your CLI based note pad")

def note():
    while True:
        what_user = input("what would you like to do, write note(w), view note(v) or delete note(d) or quit(q): ").lower()
        if what_user not in ["w", "v", "d", "q"]:
             print("invalid input")
             continue

        if what_user == "w":
             take_notes()
        elif what_user == "v":
             view_note()
        elif what_user == "d":
             pass
        else:
             break

def take_notes():

    while True:
        topic = input("Enter course title or topic you are testing: ")
        is_lecture = input("Is this a personnal reading section or a lecture(online/physical)? 'yes'or'no': ").lower()
        if is_lecture not in ["yes", "no"]:
            print("Enter yes or no")
            continue
        
        if is_lecture == "no":
                name_of_tutor = input("enter name of tutor: ")
        name_of_tutor = "personal study session"

        content = input("Content of study: ")

        dict_note = {"Topic":topic, "Name of Tutor": name_of_tutor, "Content":content}

        save_note(dict_note)

        break

def view_note():
    if not read_note():
         print("Note is empty")
    print(read_note())

def save_note(dictionary):
    with open("json_file_practice.json", mode="w", encoding="utf-8") as writefile:
         json.dump(dictionary, writefile, indent=4)
def read_note():
    with open("json_file_practice.json", mode="r", encoding="utf-8") as readfile:
         return_json = json.load(readfile)
         return return_json

note()
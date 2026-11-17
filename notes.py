import json

path = "json_file_practice.json"

def main():
     print("Your CLI based note pad")

def note():
     
     while True:
          what_user = input("what would you like to do, write note(w), view note(v) or delete note(d) or quit(q): ").lower()
          if what_user not in ["w", "v", "d", "q"]:
               print("invalid input")
               continue

          if what_user == "w":
               dictionary = take_notes()
               item = load_note()
               item.append(dictionary)
               save_note(item)
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
          else:
               if is_lecture == "no":
                         name_of_tutor = input("enter name of tutor: ")
               name_of_tutor = "personal study session"

               content = input("Content of study: ")

               dict_note = {"Topic":topic, "Name of Tutor": name_of_tutor, "Content":content}

          return dict_note

          break



def view_note():
     try:
          returned_json = load_note()
          print(returned_json)
     except json.decoder.JSONDecodeError:
          print("file is empty")

def save_note(dictionary):
    with open(path, mode="w", encoding="utf-8") as writefile:
         json.dump(dictionary, writefile, indent=4)
def load_note():
     try:
          with open(path, mode="r", encoding="utf-8") as readfile:
               return_json = json.load(readfile)
               return return_json

     except json.decoder.JSONDecodeError:
          return []    



if __name__ == "__main__":
     note()
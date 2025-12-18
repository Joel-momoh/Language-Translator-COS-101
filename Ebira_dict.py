
Ebira_dict ={
    "Nyene" : "Good morning",
    "Anyar' oodu" : "Good afternoon",
    "Ngwao " : "Hello",
    "Nyasse " : "Welcome",
    "Otura geri " : "Car",
    "Na" : "Go",
    "be" : "Come",
    "Oose" : "Walk ",
    "Avo" : "Thanks",
    "Ha" : "Wake",
    "Su' ara" : "Sleep",
    "Eyi" : "Hair",
    "Iresi" : "Head",
    "Ize" : "Wealth",
    "Engworo" : "Peace",
    "Ohu" : "Market",
    " " : " ",
    " " : " ",
    " " : " ",
    " " : " ",
}
#Ask  user for input
word= input("Enter an Ebira word:").lower()
#chech for word
if word in Ebira_dict:
    print(f"The English meaning of '{word}' is: {Ebira_dict[word]}")
else:
    print("Sorry, that word is not in the dictionary.")

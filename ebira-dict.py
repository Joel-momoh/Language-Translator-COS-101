
Ebira_dict ={
    "nyene" : "good morning",
    "anyar' oodu" : "good afternoon",
    "ngwao " : "hello",
    "nyasse " : "welcome",
    "otura geri " : "car",
    "na" : "go",
    "be" : "come",
    "oose" : "walk ",
    "avo" : "thanks",
    "ha" : "wake",
    "su' ara" : "sleep",
    "eyi" : "hair",
    "iresi" : "head",
    "ize" : "wealth",
    "engworo" : "peace",
    "ohu" : "market",
    "ira" : "light",
    "akoro" : "weldone",
    "ampo" : "bag",
    "garawa" : "bucket",
}
#Ask  user for input
word= input("Enter an Ebira word:").lower()
#chech for word
if word in Ebira_dict:
    print(f"The English meaning of '{word}' is: {Ebira_dict[word]}")
else:
    print("Sorry, that word is not in the dictionary.")


hausa_dict = {
    "sannu": "hello",
    "ina kwana": "good morning",
    "lafiya": "fine",
    "ina wuni": "good evening",
    "sai da safe": "good night",
    "sai an jima": "good bye",
    "yaya kake": "how are you?",
    "ina lafiya": "i am fine",
    "na gode sosai": "thank you very much",
    "don allah bari na tambaye ka": "excuse me please, may i ask you?",
    "yi hakuri": "i am sorry",
    "me kake nufi?": "what do you mean?",
    "ya yi daidai": "that is very good",
    "babu komai": "no problem",
    "ban gane ba": "i dont understand",
    "mene ne wannan?": "what is this?",
    "barka, sunana beulah": "hi, my name is beulah",
    "na yi farin ciki da na gamu da ke": "nice to meet you",
    "daga ina ki zo?": "where are you from",
    "daga kaduna na zo": "i am from kaduna",
}

print("barke da zuwa kamus na hausa!")
print("rubuta kalmar hausa domin ganin ma'anarta a turanci.")
print("rubuta 'fita' don rufewa./n")

while True:
    word = input("shigar da kalmar hausa:").lower()

    if word == "fita":
        print("na gode! sai anjima")
        break

    if word in hausa_dictionary:
        print("ma'anarta a turanci ita ce:", hausa_dictionary[world])
    else:
        print("yi hakuri, wannan kalma ba ta cikin kamus.")
        



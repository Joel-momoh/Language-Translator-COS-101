import streamlit as st

st.title("Language Translator")

languages = {
    "Ebira": {
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
    },
    "Igala": {
        "awa":'weldone',
        "agba':'ThankYou",
        "ona":"tomorrow",
        "una":"fire",
        "omi":"water",
        "ikpolo":"stone",
        "eju_ona":"road",
        "eja":"fish",
        "ujewn":"food",
        "otakada":"book",
        "shekpulu":"school",
        "eda":"shoe",
        "ejo":"snake",
        "usha":"pot",
        "ikpa":"bag",
        "akpe":"scorpion",
        "abia":"dog",
        "obala":"cat",
        "ugba":"plate",
        "obe":"knive",
        "oche":"soap"
     },
    "Hausa": {
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
        "daga kaduna na zo": "i am from kaduna"
    },
    "Akwaibom": {
        "afon": "good",
        "ndidia": "food",
        "mmong": "water",
        "mbonomi": "family",
        "ufokgwet": "school",
        "eyen": "baby",
        "ufok": "house",
        "abasi": "god",
        "ubong": "king",
        "ete": "father",
        "eka": "mother",
        "uduak": "time",
        "ekpe": "lion",
        "usan": "plate",
        "ekpaan": "spoon",
        "afu": "you",
        "tie": "sitdown",
        "di": "come",
        "sosong": "thankyou",
        "daka": "go"
    }
}

selection = st.selectbox("Select a language:", list(languages.keys()))

if selection:
    st.subheader(f"{selection} Dictionary")
    
    current_dict = languages[selection]
    
    user_input = st.text_input(f"Enter a word in {selection}:").lower().strip()
    
    if st.button("Translate"):
        if user_input:
            if user_input in current_dict:
                st.success(f"English Translation: {current_dict[user_input]}")
            else:
                st.info("Word not found in this dictionary.")
        else:
            st.warning("Please type a word first.")

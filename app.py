import streamlit as st

st.title("Language Translator")

languages = {
    "Ebira": {
        
        
    },
    "Hausa": {
        "sannu": "hello",
        "gida": "house",
        "ruwa": "water",
        "abinci": "food",
        "kwana": "sleep"
        
    },
    "Akwaibom": {
        "abaudie": "how are you",
        "mesiere": "good morning",
        "edi": "come",
        "tie": "sit",
        "idat": "mad"
        
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

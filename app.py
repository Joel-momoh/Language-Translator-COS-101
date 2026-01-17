import streamlit as st
import importlib
import os

st.title("Language Translator")

# This looks at your files like Akwaibom-dict.py, IGALA_DICT.py, etc.
file_list = [f for f in os.listdir('.') if f.endswith('.py') and f != 'app.py']
languages = [f.replace('.py', '') for f in file_list]

selection = st.selectbox("Select a language:", languages)

if selection:
    # This opens the file you selected from the list
    module = importlib.import_module(selection)
    
    # This pulls the 'main_dict' variable from that file
    if hasattr(module, 'main_dict'):
        dictionary = getattr(module, 'main_dict')
        
        user_input = st.text_input(f"Enter a word in {selection}:").lower().strip()

        if user_input:
            if user_input in dictionary:
                translation = dictionary[user_input]
                st.write("English translation:")
                st.success(translation)
            else:
                st.error("Word not found in this dictionary.")
    else:
        st.error(f"The file {selection}.py is missing the 'main_dict' list.")

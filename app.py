import streamlit as st
import importlib
import os

st.title("Language Translator")

file_list = [f for f in os.listdir('.') if f.endswith('.py') and f != 'app.py']

display_names = {}
for f in file_list:
    raw_name = f.replace('.py', '')
    clean_name = raw_name.replace('dict', '').replace('', ' ').title().strip()
    display_names[clean_name] = raw_name

selected_language = st.selectbox("Select a language:", list(display_names.keys()))

if selected_language:
    file_to_import = display_names[selected_language]
    
    try:
        module = importlib.import_module(file_to_import)
        
        dictionary = None
        for attribute in dir(module):
            if attribute.endswith('_dict'):
                dictionary = getattr(module, attribute)
                break
        
        if dictionary:
            st.subheader(f"{selected_language} Dictionary")
            user_input = st.text_input(f"Enter a word in {selected_language}:").lower().strip()
            
            # This adds the button you asked for
            if st.button("Translate"):
                if user_input:
                    if user_input in dictionary:
                        st.success(f"English Translation: {dictionary[user_input]}")
                    else:
                        st.info("Word not found in this dictionary.")
                else:
                    st.warning("Please type a word first.")
        else:
            st.error("Error: Could not find the dictionary list inside the file.")
            
    except Exception as e:
        st.error("Error: Ensure the file name has no dashes and is formatted correctly.")

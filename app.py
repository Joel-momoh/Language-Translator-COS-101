import streamlit as st
import importlib
import os

st.title("Language Translator")

file_list = [f for f in os.listdir('.') if f.endswith('.py') and f != 'app.py']

display_names = {}
for f in file_list:
    raw_name = f.replace('.py', '')
    clean_name = raw_name.replace('dict', '').replace('-', ' ').replace('', ' ').strip().upper()
    display_names[clean_name] = raw_name

selected_language = st.selectbox("Select a language:", list(display_names.keys()))

if selected_language:
    file_to_import = display_names[selected_language]
    
    try:
        module = importlib.import_module(file_to_import)
        
        dictionary = None
        for attribute in dir(module):
            if attribute.endswith('_dict') or attribute == 'main_dict':
                dictionary = getattr(module, attribute)
                break
        
        if dictionary:
            st.subheader(f"{selected_language} Dictionary")
            user_input = st.text_input(f"Enter a word in {selected_language}:").lower().strip()
            
            if st.button("Translate"):
                if user_input:
                    if user_input in dictionary:
                        st.success(f"English Translation: {dictionary[user_input]}")
                    else:
                        st.info("Word not found.")
                else:
                    st.warning("Please type a word.")
        else:
            st.error("Error: Dictionary list not found in file.")
            
    except Exception as e:
        st.error(f"Error loading {selected_language}. Please check the filename on GitHub.")

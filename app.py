import streamlit as st
import importlib

st.title("Language Translator")

# This is the "Better Way" - we manually map the Name to the Filename
# Left side is what people see, Right side is the exact filename on GitHub
languages = {
    "Ebira": "ebira_dict",
    "Hausa": "hausa",
    "Akwaibom": "Akwaibom_dict",
    "Igala": "IGALA_DICT"
}

selection = st.selectbox("Select a language:", list(languages.keys()))

if selection:
    # Get the filename from our map above
    file_to_load = languages[selection]
    
    try:
        # Import the file
        module = importlib.import_module(file_to_load)
        
        # Look for the dictionary list inside that file
        dictionary = None
        for attribute in dir(module):
            if attribute.endswith('_dict') or attribute == 'main_dict':
                dictionary = getattr(module, attribute)
                break
        
        if dictionary:
            st.subheader(f"{selection} Dictionary")
            user_input = st.text_input(f"Enter a word in {selection}:").lower().strip()
            
            if st.button("Translate"):
                if user_input:
                    if user_input in dictionary:
                        st.success(f"English Translation: {dictionary[user_input]}")
                    else:
                        st.info("Word not found.")
                else:
                    st.warning("Please type a word.")
        else:
            st.error(f"Could not find the word list inside the {selection} file.")
            
    except Exception as e:
        st.error(f"The app cannot find the file named '{file_to_load}.py' on GitHub. Please check your spelling.")

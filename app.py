import streamlit as st
import pickle




@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


model_path = 'trie.pkl'
trie = load_model(model_path)


def main():
    st.title("Welcome to VeePee")
    user_input = st.text_input("Start typing here...")

    if user_input:
        results = trie.autocomple(user_input.lower())
        for result in results:
            st.write(result)


if __name__ == "__main__":
    main()

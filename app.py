import streamlit as st
import pickle
import bz2file as bz2
from trie_model import Trie
from trie_model import TrieNode

@st.cache_resource

def decompress_pickle(file):
        model = bz2.BZ2File(file, 'rb')
        model = pickle.load(model)
        return model

def main():
    st.title("Welcome to VeePee")
    user_input = st.text_input("Start typing here...")
    model_path = 'trie_pkl.pbz2'
    trie = decompress_pickle(model_path)
    if user_input:
        results = trie.autocomple(user_input.lower())
        for result in results:
            st.write(result)


if __name__ == "__main__":
    main()

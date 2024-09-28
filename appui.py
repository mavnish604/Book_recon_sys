import streamlit as st
import pickle
import numpy as np
from scipy.sparse import load_npz
import requests

def load_sparse_matrix(filename):
    return load_npz(filename)

def get_similar_books(book_index, simi_matrix, n=10):
    similarities = simi_matrix[book_index].toarray().flatten()
    similar_indices = np.argsort(similarities)[::-1][1:n+1]
    return similar_indices

def recon(book, book_list, simi_matrix):
    book_index = book_list[book_list['Title'] == book].index[0]
    similar_indices = get_similar_books(book_index, simi_matrix)
    return book_list.iloc[similar_indices]['Title'].tolist()

def fetch_book_data(title):
    query = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(query)
    if response.status_code == 200:
        data = response.json()
        if "docs" in data and data["docs"]:
            book_data = data["docs"][0]
            cover_id = book_data.get("cover_i")
            cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else None
            key = book_data.get("key")
            book_url = f"https://openlibrary.org{key}" if key else None
            return cover_url, book_url
    return None, None  

simi_matrix = load_sparse_matrix("simi_sparse.npz")


with open("books.pkl", "rb") as f:
    book_list = pickle.load(f)

st.title("Book Recommender System")

book_titles = book_list["Title"].values
option = st.selectbox("Select a book", book_titles)

if st.button("Recommend"):
    st.write(f"Books similar to '{option}' are:")

    recommendations = recon(option, book_list, simi_matrix)
    
    for book in recommendations:
        st.write(f"**{book}**")
        cover_url, book_url = fetch_book_data(book)
        col1, col2 = st.columns([1, 4])
        with col1:
            if cover_url:
                st.image(cover_url, width=100)  
            else:
                st.write("No cover available")
        with col2:
            if book_url:
                st.markdown(f"[{book}]({book_url})")  
            else:
                st.write(book)  

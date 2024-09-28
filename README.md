Book Recommender System
This repository contains a book recommender system that uses a content-based filtering approach. It includes data cleaning, text preprocessing, and similarity-based recommendations. A Streamlit UI is also provided for an interactive experience.

Project Overview
The Book Recommender System allows users to get personalized book recommendations based on the book they select. The system uses a combination of text preprocessing, stemming, and a similarity matrix generated from book metadata (such as authors, categories, and descriptions) to suggest similar books.

Key Features:
Data Preprocessing: Cleans and processes book metadata, including authors, descriptions, and categories.
Text Processing: Uses tokenization, stemming, and removal of special characters for clean input.
Similarity Calculation: Utilizes a cosine similarity matrix on a vectorized representation of book tags.
Efficient Storage: Stores the similarity matrix as a sparse matrix to reduce memory usage.
Interactive UI with Streamlit: Provides an interface where users can select a book and receive recommendations, along with book covers and links.
Files and Directories
BooksDatasetClean.csv: The cleaned dataset containing book metadata (authors, titles, descriptions, categories, etc.).
books.pkl: Pickled file containing the processed book data with tags for recommendations.
simi_sparse.npz: A compressed sparse matrix of book similarities.
simi.pkl: Pickled file of the original similarity matrix before converting to sparse format.
recommender.py: Script that processes the data and calculates recommendations.
app.py: Streamlit application for interactive book recommendations.
requirements.txt: Contains the required libraries for the project (e.g., pandas, nltk, sklearn, streamlit).
Setup Instructions
1. Data Preprocessing and Building the Model
The recommender.py script processes the book dataset and generates a similarity matrix based on the following steps:

Load and clean the dataset.
Text preprocessing (lowercasing, stemming, removing special characters).
Build a tags feature from the metadata (author, description, category, publisher).
Use CountVectorizer to convert tags into vectors.
Calculate cosine similarity between books based on these vectors.
Save the resulting similarity matrix as a sparse matrix to reduce memory consumption.
Run the script:

bash
Copy code
python recommender.py
2. Streamlit Application
The Streamlit app provides a user-friendly interface to explore book recommendations.

Key Components:

Users select a book from a dropdown menu.
The system retrieves similar books using the precomputed similarity matrix.
Displays book covers and links using the OpenLibrary API.
Run the app:

bash
Copy code
streamlit run app.py
3. Dependencies
Install the required dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
4. Using the App
Once the Streamlit app is running, follow these steps:

Select a book from the dropdown menu.
Click on "Recommend" to view a list of similar books.
The recommendations will display along with their cover images and links to the OpenLibrary website.
How It Works
Data Preprocessing: The system cleans the dataset by removing null values and unnecessary columns. It also tokenizes and processes text fields like Authors, Description, and Category by converting them to lowercase, removing special characters, and performing stemming.

Creating the Similarity Matrix: A CountVectorizer is used to create vectorized representations of book metadata (tags). A cosine similarity matrix is then generated to find similar books based on this vectorized data.

Book Recommendation: Given a selected book, the system looks up the similarity matrix and retrieves the most similar books. These are displayed in the UI with additional information such as cover images and links to more details.

Credits
Data Source: Book data used for recommendations comes from an external dataset.
Cover Images & Book Links: Retrieved using the OpenLibrary API.

import pandas as pd
import numpy as np  # Make sure to import numpy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
data = pd.read_csv('./excel/BBC_News_Data_Edited.csv')  # Adjust the path if different

# Check the column names and ensure we're using the correct one for text data
print("Data columns:", data.columns)  # This will help confirm the text column name

# Use the correct column name based on your dataset structure, this example uses 'content'
ColName = 'Title Header'
#ColName = 'Title'
text_data = data[ColName] if ColName in data.columns else data[data.columns[1]]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')

# Fit and transform the text data
tfidf_matrix = vectorizer.fit_transform(text_data.values.astype('U'))

# Extract the feature names (keywords) based on TF-IDF score
feature_array = np.array(vectorizer.get_feature_names_out())
tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]

# Get the top 15 keywords
top_keywords = feature_array[tfidf_sorting][:20]

print("Top 15 Keywords:")
print(top_keywords)



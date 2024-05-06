import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def clean_text(text):
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', str(text), re.I|re.A)
    text = text.lower()
    text = text.strip()
    return text

def load_data(filepath):
    # Load the dataset
    data = pd.read_csv(filepath)
    print("Data loaded successfully.")
    return data

def preprocess_data(data, text_column):
    # Clean the data
    data['cleaned_text'] = data[text_column].apply(clean_text)
    print("Data preprocessed successfully.")
    return data

def vectorize_text(data):
    # Convert text to features using TF-IDF
    vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(data['cleaned_text'])
    print("Text vectorization complete.")
    return tfidf_matrix

def cluster_articles(tfidf_matrix, num_clusters=5):
    # Create and fit the KMeans model
    km = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = km.fit_predict(tfidf_matrix)
    print("Clustering complete.")
    return clusters

def visualize_clusters(tfidf_matrix, clusters):
    # Reduce dimensions for visualization
    pca = PCA(n_components=2)
    reduced_features = pca.fit_transform(tfidf_matrix.toarray())

    # Plot clusters
    plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=clusters)
    plt.title("Article Clusters")
    plt.xlabel("Feature space 1")
    plt.ylabel("Feature space 2")
    plt.colorbar()
    plt.show()

def main():
    filepath = './BBC News Data Only.csv'  # Replace with your file path
    text_column = 'Title Header'  # Replace with the column containing text
    data = load_data(filepath)
    data = preprocess_data(data, text_column)
    tfidf_matrix = vectorize_text(data)
    clusters = cluster_articles(tfidf_matrix, num_clusters=5)
    data['Cluster'] = clusters

    # Assuming 'data' is your DataFrame and it includes a 'Cluster' column
    # print(data['Cluster'].unique())

    for cluster in sorted(data['Cluster'].unique()):
        print(f"\nCluster {cluster} Top Words:")
        cluster_data = data[data['Cluster'] == cluster]
        all_words = ' '.join(cluster_data['cleaned_text']).split()
        most_common = pd.Series(all_words).value_counts().head(10)
        print(most_common)

    for cluster in sorted(data['Cluster'].unique()):
        text = ' '.join(data[data['Cluster'] == cluster]['cleaned_text'])
        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        #plt.title(f"Cluster {cluster} Word Cloud")
        plt.show()
        
    #print(text)
    visualize_clusters(tfidf_matrix, clusters)

if __name__ == "__main__":
    main()

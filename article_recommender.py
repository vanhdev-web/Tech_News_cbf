import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from ydata_profiling import ProfileReport



data = pd.read_csv("articles.csv", encoding= "latin-1")
data = data.drop_duplicates()

# # data visualization HTLM
# profile = ProfileReport(data, explorative=True, title="Article Report")
# profile.to_file('article_recommendation_report.html')

vectorizer = TfidfVectorizer(stop_words= "english")
tfidf_matrix = vectorizer.fit_transform(data["Article"])
tfidf_matrix_dense = pd.DataFrame(tfidf_matrix.todense(), index = data["Title"], columns = vectorizer.get_feature_names_out())

print(vectorizer.vocabulary_)
print(tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_dense = pd.DataFrame(cosine_sim, index = data["Title"], columns= data["Title"])

input_article = "Multinomial Naive Bayes in Machine Learning"
result = cosine_sim_dense.loc[input_article].sort_values(ascending=False)
print(result)


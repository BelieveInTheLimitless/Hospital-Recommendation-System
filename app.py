from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
import nltk
import re
import string
import sys
import logging

suburbs = []
subs = open('areas.txt', 'r')
for line in subs:
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.strip()
    suburbs.append(line)
subs.close
print(suburbs)


app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
	
	filenames = []
    for i in range(0, len(suburbs)):
        filenames.append("./Reviews/"+str(suburbs[i])+"/reviews.csv")
	
	# merging two csv files
    df = pd.concat(
        map(pd.read_csv, filenames), ignore_index=True)

	review_remove_translated = []

    reviews_dict = df.to_dict('list')

    for review in reviews_dict['Review']:
        review_sep = str(review).split("(Translated by Google) ")
  
     # Jika terdapat (Translated by Google)
    if review_sep[0] == "":
        review_sep = ("".join(review_sep)).split("(Original)")
        review_sep = review_sep[0]
        review = "".join(review_sep)
  
    review_remove_translated.append(review)

	reviews_dict['Review'] = review_remove_translated
    df = pd.DataFrame(reviews_dict)



	# BEGIN: PREPROCESSING

	# 1. Cleaning the text
	def clean_review(review):
		return re.sub('[^a-zA-Z]', ' ', review).lower()

	# Labeling review based on rating
	df['cleaned_review'] = df['Review'].apply(lambda x: clean_review(str(x)))
	df['label'] = df['Rating'].map({"1 star":0, "2 stars":0, "3 stars":0, "4 stars":1, "5 stars":1})


	# 2. Adding additional features -> length of, and percentage of punctuations in the text
	def count_punct(review):
		count = sum([1 for char in review if char in string.punctuation])
		return round(count/(len(review) - review.count(" ")), 3)*100

	df['review_len'] = df['Review'].apply(lambda x: len(str(x)) - str(x).count(" "))
	df['punct'] = df['Review'].apply(lambda x: count_punct(str(x)))


	# 3. Tokenization
	def tokenize_review(review):
		tokenized_review = review.split()
		return tokenized_review

	df['tokens'] = df['cleaned_review'].apply(lambda x: tokenize_review(x))


	# 4. Lemmatization and Removing Stopwords
	all_stopwords = stopwords.words('english')
	all_stopwords.remove('not')
	def lemmatize_review(token_list):
		return " ".join([lemmatizer.lemmatize(token) for token in token_list if not token in set(all_stopwords)])

	lemmatizer = nltk.stem.WordNetLemmatizer()
	df['lemmatized_review'] = df['tokens'].apply(lambda x: lemmatize_review(x))

	# END: PREPROCESSING



	# FEATURE EXTRACTION (TF-IDF)
	X = df[['lemmatized_review', 'review_len', 'punct']]
	y = df['label']
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
	# ignore terms that occur in more than 50% documents and the ones that occur in less than 2
	tfidf = TfidfVectorizer(max_df=0.5, min_df=2)
	tfidf_train = tfidf.fit_transform(X_train['lemmatized_review'])
	tfidf_test = tfidf.transform(X_test['lemmatized_review'])



	# PREDICTION
	classifier = SVC(kernel= 'linear', random_state = 10)
	classifier.fit(tfidf_train, y_train)
	classifier.score(tfidf_test, y_test)
	





	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = tfidf.transform(data).toarray()
		prediction = classifier.predict(vect)
	return f"{prediction[0]}"


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
	app.run(debug=True)
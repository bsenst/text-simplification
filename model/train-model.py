import textstat
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data_url = "https://raw.githubusercontent.com/babaknaderi/TextComplexityDE/master/TextComplexityDE19/parallel_corpus.csv"
parallel = pd.read_csv(data_url, encoding="latin-1")

metrics = {
    "flesch_reading_ease":textstat.flesch_reading_ease,
    "flesch_kincaid_grade":textstat.flesch_kincaid_grade,
    "smog_index":textstat.smog_index,
    "coleman_liau_index":textstat.coleman_liau_index,
    "automated_readability_index":textstat.automated_readability_index,
    "dale_chall_readability_score":textstat.dale_chall_readability_score,
    "difficult_words":textstat.difficult_words,
    "linsear_write_formula":textstat.linsear_write_formula,
    "gunning_fog":textstat.gunning_fog,
    "fernandez_huerta":textstat.fernandez_huerta,
    "szigriszt_pazos":textstat.szigriszt_pazos,
    "gutierrez_polini":textstat.gutierrez_polini,
    "crawford":textstat.crawford,
    "gulpease_index":textstat.gulpease_index,
    "osman":textstat.osman,
}

results = []

for sentence in parallel.Original_Sentence:
    result_part = []
    for key in metrics.keys():
        result_part.append(metrics[key](sentence))
    results.append(result_part)

df1 = pd.DataFrame(results)

results = []

for sentence in parallel.Simplification:
    result_part = []
    for key in metrics.keys():
        result_part.append(metrics[key](sentence))
    results.append(result_part)

df2 = pd.DataFrame(results)

df = df1 - df2

rating_map = {
    "Nicht einfacher / konnte nicht vereinfacht werden":0,
    "Etwas einfacher":1,
    "Deutlich einfacher":2,
}

df["rating"] = parallel.Rating.map(rating_map)

df = df[df.rating!=0]

# Assuming your DataFrame is named 'df'
# Separate features and target variable
X = df.drop('rating', axis=1)
y = df['rating']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes classifier
model = GaussianNB()

# Train the model on the training set
model.fit(X_train, y_train)

# Save the model using pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
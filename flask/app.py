from flask import Flask, request, jsonify
import textstat
import pandas as pd
import pickle

app = Flask(__name__)

metrics = {
    "flesch_reading_ease": textstat.flesch_reading_ease,
    "flesch_kincaid_grade": textstat.flesch_kincaid_grade,
    "smog_index": textstat.smog_index,
    "coleman_liau_index": textstat.coleman_liau_index,
    "automated_readability_index": textstat.automated_readability_index,
    "dale_chall_readability_score": textstat.dale_chall_readability_score,
    "difficult_words": textstat.difficult_words,
    "linsear_write_formula": textstat.linsear_write_formula,
    "gunning_fog": textstat.gunning_fog,
    "fernandez_huerta": textstat.fernandez_huerta,
    "szigriszt_pazos": textstat.szigriszt_pazos,
    "gutierrez_polini": textstat.gutierrez_polini,
    "crawford": textstat.crawford,
    "gulpease_index": textstat.gulpease_index,
    "osman": textstat.osman,
}

# Load the model using pickle
with open('model/model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        examples = data['examples']

        result_part0 = []
        for key in metrics.keys():
            result_part0.append(metrics[key](examples[0]))

        result_part1 = []
        for key in metrics.keys():
            result_part1.append(metrics[key](examples[1]))

        result_df = pd.DataFrame(result_part0) - pd.DataFrame(result_part1)

        prediction = loaded_model.predict(result_df.T)[0]

        return jsonify({'prediction': ['no good simplification', 'good simplification'][prediction-1]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)

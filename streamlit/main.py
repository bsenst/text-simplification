import streamlit as st
import textstat
import pandas as pd
import pickle

st.title("Text Simplification Evaluation")

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

example_std = """Während der aktuellen COVID-19-Pandemie ist die schnelle Verfügbarkeit fundierter
Informationen von entscheidender Bedeutung, um Informationen über Diagnose, Krankheitsverlauf, 
Behandlung abzuleiten oder die Verhaltensregeln in der Öffentlichkeit anzupassen."""

example_easy = """Während der aktuellen COVID-19-Pandemie ist es wichtig, dass wir schnell an 
fundierte Informationen gelangen können. Diese Informationen sind entscheidend, um mehr über 
die Diagnose, den Krankheitsverlauf und die Behandlung zu erfahren. Außerdem helfen sie dabei, 
die Verhaltensregeln in der Öffentlichkeit anzupassen."""

std = st.text_area("Standard Version", example_std, height=100)
easy = st.text_area("Simplified Version", example_easy, height=130)

st.caption("""The example text is cited from: Langnickel, Lisa and Baum, Roman and Darms, Johannes and
 Madan, Sumit and Fluck, Juliane. COVID-19 preVIEW: Semantic Search to Explore COVID-19 Research 
 Preprints. 2021. DOI: 10.3233/SHTI210124""")

if st.button("Evaluate Simplification"):

    result_part0 = []
    for key in metrics.keys():
        result_part0.append(metrics[key](std))

    result_part1 = []
    for key in metrics.keys():
        result_part1.append(metrics[key](easy))

    result_df = pd.DataFrame(result_part0) - pd.DataFrame(result_part1)

    prediction = loaded_model.predict(result_df.T)[0]

    st.success([':thumbsdown: no good simplification ', ':thumbsup: good simplification'][prediction-1])
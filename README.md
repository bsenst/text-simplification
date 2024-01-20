# text-simplification

## Problem Description

In today's digital age, information accessibility is of paramount importance. However, a significant barrier exists for individuals with varying levels of language proficiency when encountering complex texts. To address this challenge, the field of text simplification has emerged, aiming to create versions of text that are easier to comprehend while retaining essential information. The project aims to evaluate the efficacy of simplified text translations.

## Exploratory Data Analysis

Have a look on the training dataset and the text metrics in the [EDA notebook](https://github.com/bsenst/text-simplification/blob/main/notebooks/explore-data-and-metrics.ipynb).

The model was trained on the parallel corpus from:
> https://github.com/babaknaderi/TextComplexityDE

## Model Training Notebook

The [model training notebook](https://github.com/bsenst/text-simplification/blob/main/notebooks/train-easyfication-classifier.ipynb) and comparison of different machine learning algorithms (Logistic Regression, Random Forest, GaussianNB).

## Exporting Model Training to Script

The training script and the final model can be found in the [model folder](https://github.com/bsenst/text-simplification/tree/main/model).

## Reproducibility, Dependencies & Environment Management

Create a Python virtual environment:
`$ python -m venv .env`

Activate the Python virtual environment:
`$ source .env/bin/activate`

Install the required dependencies:
`(.env) $ pip install -r requirements.txt`

## Model Deployment with Flask

Run the Flask app in your local environment with:
`(.env) $ python flask/app.py`

Post the example texts and get the evaluation for simplification success:
```
curl -X POST -H "Content-Type: application/json" -d '{
  "examples": [
    "Während der aktuellen COVID-19-Pandemie ist die schnelle Verfügbarkeit fundierter Informationen von entscheidender Bedeutung, um Informationen über Diagnose, Krankheitsverlauf, Behandlung abzuleiten oder die Verhaltensregeln in der Öffentlichkeit anzupassen.",
    "Während der aktuellen COVID-19-Pandemie ist es wichtig, dass wir schnell an fundierte Informationen gelangen können. Diese Informationen sind entscheidend, um mehr über die Diagnose, den Krankheitsverlauf und die Behandlung zu erfahren. Außerdem helfen sie dabei, die Verhaltensregeln in der Öffentlichkeit anzupassen."
  ]
}' http://127.0.0.1:5000/predict
```

This example text is cited from:
> Langnickel, Lisa and Baum, Roman and Darms, Johannes and Madan, Sumit and Fluck, Juliane. COVID-19 preVIEW: Semantic Search to Explore COVID-19 Research Preprints. 2021. DOI: 10.3233/SHTI210124

## Model Deployment with Streamlit

Run the streamlit app in your local environment with:
`(.env) $ python -m streamlit run streamlit/main.py`

## Containerization Flask

To create the docker image:
`(.env) $ docker build -t flask-app -f Dockerfile_Flask .`

To run the docker image:
`(.env) $ docker run -p 5000:5000 flask-app`

## Containerization Streamlit

To create the docker image:
`(.env) $ docker build -t streamlit-app -f Dockerfile_Streamlit .`

To run the docker image:
`(.env) $ docker run -p 8501:8501 streamlit-app`

## Cloud Deployment

![screenshot-streamlit-app](https://github.com/bsenst/text-simplification/assets/8211411/8ea6a041-c4fa-4dba-9dde-bee5990e7a58)

https://text-simplification-evaluation.streamlit.app/

## References

The example text was translated with ChatGPT into easy language originally is cited from:
> Langnickel, Lisa and Baum, Roman and Darms, Johannes and Madan, Sumit and Fluck, Juliane. COVID-19 preVIEW: Semantic Search to Explore COVID-19 Research Preprints. 2021. DOI: 10.3233/SHTI210124

The model was trained on the parallel corpus from:
> https://github.com/babaknaderi/TextComplexityDE

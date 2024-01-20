# text-simplification

## Problem Description

In today's digital age, information accessibility is of paramount importance. However, a significant barrier exists for individuals with varying levels of language proficiency when encountering complex texts. To address this challenge, the field of text simplification has emerged, aiming to create versions of text that are easier to comprehend while retaining essential information. The project aims to evaluate the efficacy of simplified text translations.

## Exploratory Data Analysis

## Model Training

## Exporting Model to Script

## Reproducibility, Dependencies & Environment Management

`$ python -m venv .env`

`$ source .env/bin/activate`

`(.env) $ pip install -r requirements.txt`

## Model Deployment with Flask

`(.env) $ python flask/app.py`

```
curl -X POST -H "Content-Type: application/json" -d '{
  "examples": [
    "Während der aktuellen COVID-19-Pandemie ist die schnelle Verfügbarkeit fundierter Informationen von entscheidender Bedeutung, um Informationen über Diagnose, Krankheitsverlauf, Behandlung abzuleiten oder die Verhaltensregeln in der Öffentlichkeit anzupassen.",
    "Während der aktuellen COVID-19-Pandemie ist es wichtig, dass wir schnell an fundierte Informationen gelangen können. Diese Informationen sind entscheidend, um mehr über die Diagnose, den Krankheitsverlauf und die Behandlung zu erfahren. Außerdem helfen sie dabei, die Verhaltensregeln in der Öffentlichkeit anzupassen."
  ]
}' http://127.0.0.1:5000/predict
```

## Model Deployment with Streamlit

`(.env) $ python -m streamlit run streamlit/main.py`

## Containerization

## Cloud Deployment

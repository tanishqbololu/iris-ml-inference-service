# Iris ML Inference Service

Production-ready machine learning inference service for Iris flower classification,
built using **BentoML** and **Docker**.

This project demonstrates how to package a trained ML model into a reproducible,
containerized API suitable for real-world deployment.

---

## 🚀 Features

- Scikit-learn based classification model
- REST API for real-time inference
- BentoML for model packaging and serving
- Fully Dockerized deployment
- Reproducible and versioned ML artifacts

---

## 🧠 Model Details

- **Algorithm:** Support Vector Classifier (SVC)
- **Dataset:** Iris dataset
- **Input:** 4 numerical features  
  (`sepal_length`, `sepal_width`, `petal_length`, `petal_width`)
- **Output:** Class index (`0`, `1`, `2`)

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- BentoML
- Docker

---

## 📁 Project Structure

iris-ml-inference-service/

├── service.py # BentoML service definition (API)

├── train.py # Model training and saving script

├── test.py # Model testing

├── bentofile.yaml # Bento build configuration

├── requirements.txt

├── README.md

└── .gitignore

## ▶️ Run Locally (Development)

Serve directly from source code:
```bash
bentoml serve service:IrisService --reload
```

Swagger UI will be available at:
http://localhost:3000

To stop the server, press CTRL + C.

---

## 🐳 Run with Docker

1) Build the Bento
```bash
bentoml build
```
2) Create Docker image
```bash
bentoml containerize iris_classifier:latest
```
3) Run the container
```bash
docker run -p 3000:3000 iris_classifier:latest
```
---

## 🔍 Test the API
```bash
curl -X POST http://localhost:3000/classify \
  -H "Content-Type: application/json" \
  -d "[[5.1, 3.5, 1.4, 0.2]]"
```
Example response: [0]


📈 Production Notes

* Models and dependencies are versioned using BentoML
* Docker image is portable across environments
* Suitable for deployment on cloud VMs, Kubernetes, or managed platforms
* Health check and metrics endpoints are available out of the box

🧩 Future Improvements

* Input validation and schema enforcement
* Batch inference endpoint
* Authentication and rate limiting
* Cloud deployment (AWS / Azure / GCP)
* Monitoring and logging integration
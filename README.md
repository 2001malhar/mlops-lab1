# Iris Prediction API - Lab Documentation

This project provides a complete Machine Learning lifecycle demonstration, from training a Decision Tree classifier on the classic Iris dataset to deploying it as a RESTful API using **FastAPI**.

---

## ## Project Overview

The lab consists of a training script that generates a model file and a web server that serves predictions. The API supports single and batch predictions, health monitoring, and a feedback loop for model evaluation.

### ### Key Features

* **Model Training**: Automated training using `scikit-learn`.
* **Single & Batch Inference**: Endpoints to process one or multiple flower samples.
* **Model Management**: Ability to view model parameters and reload the model from disk without restarting the server.
* **Feedback Mechanism**: Endpoint to log prediction accuracy for future retraining.
* **History Tracking**: In-memory storage of recent predictions.

---

## ## File Structure

```text
project-root/
│
├── model/
│   └── iris_model.pkl       # Serialized Decision Tree model
├── src/
│   ├── train.py             # Script to train and save the model
│   └── main.py              # FastAPI application logic
└── requirements.txt         # Project dependencies

```

---

## ## API Endpoints Summary

| Method | Endpoint | Description |
| --- | --- | --- |
| **GET** | `/` | Welcome message and API check. |
| **POST** | `/predict` | Predict class for a single Iris flower. |
| **POST** | `/predict/batch` | Predict classes for a list of Iris flowers. |
| **GET** | `/health` | Returns API status and model version. |
| **GET** | `/model-info` | Returns the Decision Tree hyperparameters. |
| **GET** | `/history` | Shows the last  predictions made. |
| **POST** | `/feedback` | Submit manual correction/verification of a prediction. |
| **POST** | `/system/reload-model` | Reloads `iris_model.pkl` from the filesystem. |

---

## ## Step-by-Step Setup & Execution

Follow these steps to re-run the lab from scratch:

### 1. Environment Setup

Ensure you have Python 3.10+ installed. Install the required libraries:

```bash
pip install fastapi pydantic scikit-learn joblib uvicorn numpy pandas

```

### 2. Train the Model

Before starting the server, you must generate the model file.

* Navigate to the `src/` directory.
* Run the training script:

```bash
python train.py

```

> **Note**: This will create `iris_model.pkl` in the `../model/` folder.

### 3. Launch the API

Start the FastAPI server using `uvicorn`:

```bash
uvicorn main:app --reload

```

The API will now be accessible at `http://127.0.0.1:8000`.

### 4. Testing the API

You can interact with the API using the built-in Swagger UI at `http://127.0.0.1:8000/docs` or via `curl`.

**Example Prediction Request:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'

```

---

## ## Technical Implementation Details

### Data Validation

The API utilizes **Pydantic** models (`IrisData`) to ensure that incoming requests contain the four required float values (, , , ).

### Model Logic

The model is a **Decision Tree Classifier**. The training process maps the four input features to one of three target classes:

* **0**: Setosa
* **1**: Versicolor
* **2**: Virginica

### Error Handling

The application includes custom `HTTPException` triggers. For example, if a user requests info for a `class_id` outside of 0-2, the API returns a `404 Not Found` with a helpful instruction.

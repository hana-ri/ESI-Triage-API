# ESI Triage API

![ESI-Triage](https://img.shields.io/badge/ESI-Triage-brightgreen)
![API](https://img.shields.io/badge/Flask-API-blue)
![CNN](https://img.shields.io/badge/1D-CNN-yellow)

This repository contains the implementation of an API for Emergency Severity Index (ESI) Triage level classification, utilizing a 1D CNN architecture model. The API provides endpoints to classify patients into appropriate triage levels based on their vital signs and demographic data.

## Overview

Emergency departments often face challenges with overcrowding, which can lead to delays in patient care. The ESI Triage system helps prioritize patients based on the severity of their conditions. This API serves a machine learning model that automates the triage classification process, potentially reducing wait times and improving patient outcomes.

## Model Architecture

This API deploys a pre-trained 1D Convolutional Neural Network model that was developed to classify patients into 5 ESI triage levels. The model takes patient data as input, including:

- Age
- Heart Rate (HR)
- Systolic Blood Pressure (SBP)
- Diastolic Blood Pressure (DBP)
- Respiratory Rate (RR)
- Oxygen Saturation (O2)
- Temperature

The model achieved an accuracy of 81%, outperforming traditional machine learning approaches.

## API Endpoints

- `GET /ping`: Health check endpoint to verify the API is running
- `POST /predict`: Accepts patient data in JSON format and returns the predicted ESI triage level

### Example Request

```json
{
  "age": 65,
  "triage_vital_hr": 90,
  "triage_vital_sbp": 130,
  "triage_vital_dbp": 80,
  "triage_vital_rr": 18,
  "triage_vital_o2": 96,
  "triage_vital_temp": 37.5
}
```

### Example Response

```json
{
  "result": "ESI 2"
}
```

## Installation & Setup

### Prerequisites
- Python 3.11 or later
- Docker (optional, for containerized deployment)

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/hana-ri/ESI-Triage-API.git
   cd ESI-Triage-API
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the API:
   ```
   python app.py
   ```

The API will be accessible at `http://localhost:5000`.

### Docker Deployment

1. Build the Docker image:
   ```
   docker build -t esi-triage-api .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 esi-triage-api
   ```

## Model Development

This repository contains the implementation of the model for production use. The model was developed in a separate repository, which includes the model training, evaluation, and experimentation phases:

[ESI Triage Classification Model Development Repository](https://github.com/hana-ri/Emergency-Severity-Triage-Classification)

## Research Background

This project is part of the research thesis "DESIGN OF A TRIAGE LEVEL CLASSIFICATION APPLICATION FOR IGD PATIENTS USING ONE-DIMENSIONAL CNN ARCHITECTURE" by Mohamad Rizal Hanafi.

### Research Publication
This work is based on research that was published as:

**DESIGN OF A TRIAGE LEVEL CLASSIFICATION APPLICATION FOR IGD PATIENTS USING ONE-DIMENSIONAL CNN ARCHITECTURE**  
**Author:** Mohamad Rizal Hanafi  
**Published:** 2024/2/25  
**Institution:** Universitas Pendidikan Indonesia

**Summary:**  
This research addressed emergency room overcrowding by developing a 5-level ESI triage classification system using 1D CNN architecture. The model achieved 81% accuracy (precision, recall, and f1-score of 0.81), outperforming neural networks (78%), XGBoost (75%), and logistic regression (70%). The resulting web application passed all functional testing requirements.

**Thesis Repository:** https://repository.upi.edu/120201
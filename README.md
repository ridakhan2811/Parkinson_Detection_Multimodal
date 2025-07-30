# 🧠 Parkinson_Detection_Multimodal

**Parkinson_Detection_Multimodal** is a real-time machine learning system designed to detect Parkinson’s Disease using three diverse input modalities — **Spiral Drawings**, **Voice Recordings**, and **Posture Videos**.  
It integrates image classification, audio signal analysis, pose estimation, and deep learning to deliver insightful and multimodal predictions.

---

## 🧩 Features

- Detect Parkinson’s Disease from **Spiral Drawings**, **Voice**, and **Posture**
- Predict:
  - Possibility of Parkinson’s
  - **Stage** of the disease
  - Suggested **next steps**
- Maintain **patient history** for recovery tracking
- Multimodal Fusion Model for accurate diagnosis
- Ready for future deployment in clinical tools

---

## 🧠 Technologies Used

- Python (Core ML Language)
- TensorFlow / PyTorch (Modeling)
- MediaPipe & OpenCV (Pose Detection)
- librosa & soundfile (Audio Features)
- Django (Web Backend)
- HTML / CSS / Bootstrap (Frontend)
- Git & GitHub for version control

---

## 📁 Folder Overview

- `spiral_model/` → Spiral Drawing Classification (CNN: VGG16, ResNet)
- `voice_model/` → Audio Processing (MFCC, 1D CNN, LSTM)
- `posture_model/` → Posture Tracking (MediaPipe, LSTM)
- `fusion_model/` → Combined prediction module
- `django_app/` → Web App Interface
- `data/` → Raw and processed dataset samples
- `utils/` → Helper scripts

---

## 📊 Dataset (In Progress)

- Data collected manually from Indian patients
- Augmentation planned via **Generative AI**
- Custom multimodal dataset for potential IEEE publication

---

## 👥 Team Members

- **Rida Khan**
- **Rutuja Deshmukh** 
- **Ayush Shinde**  
- **Atharva Deore** 
- **Sanchit Sonawane** 
- **Harshit Sable** 

---

## ⚠️ Disclaimer

This project is intended for **research and educational purposes only**. It is not approved for clinical diagnosis.  
Please consult certified neurologists for medical advice.

---

## 🧑‍💼 Mentorship

Developed as part of internship at **ProWorld Technology Pvt. Ltd.**  
Under the guidance of **Gokul Sir** – CEO & Project Mentor

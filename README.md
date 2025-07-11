\# 🧠 Parkinson\_Detection\_Multimodal



A real-time, multimodal machine learning project to detect Parkinson’s Disease using three diverse symptom inputs: \*\*Spiral Drawings\*\*, \*\*Voice Recordings\*\*, and \*\*Posture Videos\*\*. This project integrates computer vision, audio signal processing, pose estimation, and deep learning to provide an accurate and insightful diagnosis system.



---



\## 🚀 Project Goals



\- Detect Parkinson’s Disease based on \*\*three different inputs\*\*.

\- Predict:

&nbsp; - Whether the patient is likely to have Parkinson’s.

&nbsp; - The \*\*stage\*\* of the disease.

&nbsp; - Suggested \*\*next steps\*\* or \*\*recommended treatment paths\*\*.

\- Maintain a \*\*patient history\*\* to track progression or recovery.

\- Aim to eventually integrate this into a secure medical application usable by doctors and patients.



---



\## 🧩 Multimodal Inputs



| Symptom Type   | Input                   | Processing Technique | Model Used             |

| -------------- | ----------------------- | -------------------- | ---------------------- |

| Spiral Drawing | Static images (spirals) | Image Classification | CNN (VGG16, ResNet)    |

| Voice          | Audio (.wav)            | MFCC + Spectrogram   | 1D CNN, LSTM           |

| Posture        | Video (.mp4) or live    | Pose Extraction      | MediaPipe + CNN / LSTM |



---



\## 🛠️ Tech Stack \& Libraries



\### 🔹 Backend / Machine Learning

\- Python

\- TensorFlow / PyTorch

\- OpenCV

\- MediaPipe

\- librosa

\- NumPy

\- scikit-learn



\### 🔹 Frontend

\- Django

\- HTML / CSS (Bootstrap optional)



\### 🔹 Utilities

\- moviepy

\- matplotlib

\- soundfile

\- Pillow

\- pandas



---



\## 📁 Project Structure (Example)



Parkinson\_Detection\_Multimodal/

├── spiral\_model/ # CNN model for spiral drawings

├── voice\_model/ # Audio preprocessing + RNN models

├── posture\_model/ # Pose detection and temporal models

├── fusion\_model/ # Final classifier that integrates all

├── django\_app/ # Web interface (Django backend)

├── data/ # Sample datasets or paths

├── utils/ # Helper scripts

└── README.md



---



\## 🧪 Dataset



\- Currently collecting Indian patient data manually.

\- Data augmentation via \*\*Generative AI\*\* planned.

\- Spiral drawings, voice samples, and posture videos will be compiled into a custom IEEE-publishable dataset.



---



\## 📊 Future Plans



\- Patient History Tracking Dashboard 📈

\- Role-based Login (Doctor/Patient) 👨‍⚕️

\- PDF Report Generation 🧾

\- Integration with Real-Time Camera or Mic Inputs 📷🎤

\- Deploy on cloud (Render / AWS / Heroku)



---



\## 👥 Team Members \& Roles



| Name              | Role                                  |

|-------------------|----------------------------------------|

| \*\*Rida Khan\*\*      | Spiral Drawing Model \& Image Processing |

| \*\*Rutuja Deshmukh\*\*| Voice/Speech Processing \& ML Modeling  |

| \*\*Ayush Shinde\*\*   | Database Management \& Django Backend   |

| \*\*Atharva Deore\*\*  | Posture Detection \& Pose Estimation    |

| \*\*Sanchit Sonawane\*\*| Frontend Development (UI/UX)          |

| \*\*Harshit Sable\*\*  | Django Backend, Routing \& APIs         |



---



\## ⚠️ Disclaimer



This tool is for \*\*research and educational purposes only\*\*. It should not be used for clinical diagnosis. Always consult a certified neurologist for accurate medical advice.



---



\## 🧑‍💻 Maintained By



Developed as part of internship at \*\*ProWorld Technology Pvt. Ltd.\*\*, under the guidance of:



\- \*\*Gokul Sir\*\* – CEO \& Project Mentor

\- Team Parkinson\_Detection\_Multimodal (see above 👆)



---




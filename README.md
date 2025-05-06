# Deepfake Detection System

This project presents a **custom DenseNet-121 architecture** for detecting deepfake images, benchmarked against **InceptionResNetV2** and **VGG16**. Our proposed DenseNet-121 model achieves superior performance with a **95.91% accuracy**, outperforming InceptionResNetV2 (**93.4%**) and VGG16 (**91.5%**).

---

## 🔍 Overview

With the growing threat of manipulated media, deepfake detection has become crucial. This project focuses on developing and comparing deep learning architectures for robust detection of real vs. fake imagery. It includes:

- A custom DenseNet-121 model optimized for deepfake classification.
- Comparative analysis with InceptionResNetV2 and VGG16.
- A Streamlit web app for real-time testing.
- A research paper documenting the methodology and results.
- A Jupyter notebook for detailed experimentation.

---

## 📊 Model Performance

| Model              | Accuracy (%) |
|-------------------|--------------|
| Custom DenseNet-121 | **95.91**     |
| InceptionResNetV2 | 93.40        |
| VGG16             | 91.50        |

---

## 📁 Repository Structure

Deepfake-Detection-System/
│
├── streamlit_app/ # Streamlit-based user interface
│ └── app.py
│
├── notebooks/
│ └── model_comparison.ipynb # Contains training and testing code
│
├── models/ # Saved model weights
│
├── research/
│ └── deepfake_detection_paper.pdf # Project report and findings
│
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## 📄 Research Paper
For detailed methodology, dataset preprocessing, model architecture, and experimental results, refer to:
**Novel Technique for a DeepFake Detection System with Transfer Learning using DenseNet-121.pdf**

## 🧠 Tech Stack
- Python, TensorFlow, Keras
- DenseNet-121 (customized), InceptionResNetV2, VGG16
- Streamlit for UI
- Jupyter Notebook for experimentation

✍️ Authors
[Ilfa Shaheed]
[Ria Sanjay]
[Akash Rajasekar]


💡 Acknowledgements
- Deepfake datasets from [insert dataset name or source].
- Inspiration from recent advancements in deep learning for image forensics.

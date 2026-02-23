# 🔢 MNIST Digit Classifier with CNN 🤖  
![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow) ![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?logo=keras) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2583/2583344.png" alt="MNIST Digit Classifier Logo" width="140"/>
</p>

🚀 This project implements a **Convolutional Neural Network (CNN)** using TensorFlow/Keras to classify handwritten digits from the **MNIST dataset**. The model achieves **98.42% test accuracy** after just 5 epochs. It demonstrates a complete pipeline: loading data, preprocessing, building a CNN, training, evaluation, and making predictions on new images.

---

## ✨ Key Features  
🔢 **MNIST Dataset** – Classic handwritten digit recognition benchmark  
🧠 **CNN Architecture** – Multiple convolutional and pooling layers  
📊 **Data Preprocessing** – Normalization, reshaping, one‑hot encoding  
📈 **Training & Evaluation** – Tracks accuracy and loss, prints test accuracy  
🎨 **Visualization** – Displays a sample test image with its predicted label  
⚡ **Fast Training** – Achieves high accuracy in only 5 epochs  

---

## 🧠 Tech Stack  
- **Language:** Python 🐍  
- **Framework:** TensorFlow / Keras  
- **Libraries:** NumPy, Matplotlib  
- **Model:** Convolutional Neural Network  
- **Dataset:** MNIST (handwritten digits)  

---

## 📦 Installation  

```bash
git clone https://github.com/SayabArshad/MNIST-CNN-Image-Classifier.git
cd MNIST-CNN-Image-Classifier
pip install tensorflow matplotlib numpy
````

⚙️ Note: The MNIST dataset is automatically downloaded by TensorFlow when you run the script.

---

## ▶️ Usage

Run the main script:

```bash
python "Image classifier.py"
```

The script will:

Load and preprocess the MNIST dataset.

Build and compile the CNN model.

Train the model for 5 epochs.

Print the test accuracy.

Show a sample test image with its predicted label.

---

## 📁 Project Structure

```
MNIST-CNN-Image-Classifier/
│-- Image classifier.py                    t
│-- README.md                                
│-- assets/                                  
│    ├── code.JPG
│    ├── terminal.JPG
│    └── image classifier.JPG
```
---

## 🖼️ Interface Previews

| 📝 Code Snippet | 📊 Console Output |
|:---------------:|:-----------------:|
| ![Code Snippet](assets/code.JPG) | ![Terminal](assets/terminal.JPG) |

## 📈 Sample Prediction

![Sample Prediction](assets/image%20classifier.JPG)

---

## 💡 About the Project
Handwritten digit recognition is a classic problem in computer vision and deep learning. This project builds a CNN from scratch using Keras to classify digits from the MNIST dataset. The architecture consists of three convolutional layers with max pooling, followed by a dense layer and a softmax output. After training for only 5 epochs, the model achieves an impressive 98.42% test accuracy. The script also demonstrates how to make predictions on individual test images and visualize the results – a fundamental step toward building real‑world digit recognition systems.

---

## 🧑‍💻 Author

**Developed by:** [Sayab Arshad Soduzai](https://github.com/SayabArshad) 👨‍💻

📅 **Version:** 1.0.0

📜 **License:** MIT License

---

## ⭐ Contributions

Contributions are welcome! Fork the repository, open issues, or submit pull requests to enhance functionality (e.g., adding more layers, experimenting with different optimizers, or building a web app).
If you find this project helpful, please ⭐ star the repository to show your support.

---

## 📧 Contact

For queries, collaborations, or feedback, reach out at **[sayabarshad789@gmail.com](mailto:sayabarshad789@gmail.com)**

---

🔢 Teaching machines to read handwritten digits.

---

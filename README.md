# 🚦 Interactive Traffic Sign Recognition Web App

This project implements an end-to-end deep learning pipeline to classify German traffic signs. It features a custom **Convolutional Neural Network (CNN)** trained on the GTSRB dataset and deployed in an interactive web application for real-time video processing.

---

## 📌 Project Overview
- **Data Preprocessing**: Loaded images from CSV paths, resized them to a uniform 32×32 pixels, normalized pixel values to a [0, 1] range, and one-hot encoded the class labels.
- **Data Augmentation**: Applied on-the-fly random rotations, width/height shifts, and zoom transformations to the training data to prevent overfitting and improve generalization.
- **Model Training**: Built and trained a custom CNN architecture using TensorFlow/Keras, incorporating modern techniques like Batch Normalization and Early Stopping.
- **Interactive Web Application**: Developed a Flask-based web server with a user-friendly frontend to allow users to upload videos and view real-time predictions.
- **Real-Time Detection**: Implemented an OpenCV pipeline that isolates potential signs using color masking, passes them to the CNN for classification, and overlays bounding boxes with predicted labels onto the output video.

---

## 🛠️ Tech Stack
- **Python**
- **TensorFlow / Keras** → Building and training the deep learning model
- **Flask** → Backend web server
- **OpenCV** → Real-time video processing and image manipulation
- **NumPy, Pandas** → Data loading and manipulation
- **Matplotlib** → Generating training history plots
- **HTML, CSS, JavaScript** → Frontend user interface
- **Chart.js** → Displaying interactive performance graphs

---

## 📂 Dataset
- The **German Traffic Sign Recognition Benchmark (GTSRB)**.
- Contains over 50,000 images across **43 distinct classes** of traffic signs.
- Includes `Train.csv` and `Meta.csv` for image paths and class label information.
- Images feature significant variations in lighting, scale, rotation, and partial occlusion.

---

## 🤖 Model Implemented
- **Custom CNN Architecture**: A sequential model designed for multi-class image classification.
  - **Convolutional Layers (32, 64, 128 filters)** with (3,3) kernels and ReLU activation to learn hierarchical features.
  - **MaxPooling Layers** with a (2,2) pool size to downsample feature maps and create spatial invariance.
  - **Batch Normalization Layers** added after each convolutional block to stabilize and accelerate training.
  - **Flatten Layer** to convert 2D feature maps into a 1D vector for the classifier.
  - **Dense Fully Connected Layer (256 units)** with ReLU activation.
  - **Dropout Layer (0.5 rate)** to provide regularization and reduce overfitting.
  - **Softmax Output Layer** with 43 units for multi-class probability distribution.

---

## 📈 Model Evaluation & Insights
- Achieved high classification accuracy (>98%) on the validation set, indicating a well-fitted model.
- Data Augmentation, Batch Normalization, and Early Stopping were highly effective in preventing overfitting.
- The model demonstrates strong performance in classifying signs even under challenging real-world video conditions.
- The real-time detection pipeline successfully integrates the model, proving the viability of the end-to-end system.

---

## 🌐 Web Application Details
- **Backend (Flask)**: A lightweight Python server handles file uploads, calls the video processing script, and serves the final processed video as a static file.
- **Frontend (HTML/JS/CSS)**: A clean, single-page interface allows users to select a video file. JavaScript handles the asynchronous file upload and dynamically updates the UI to show a loading state and the final video player.
- **UI Features**: Includes a file picker, a loading indicator during processing, an embedded video player for results, and interactive charts displaying the model's training history.

---

## 📷 Visualizations
- Training vs. Validation Accuracy and Loss curves.
- Sample video frames with dynamically rendered bounding boxes and predicted sign labels.
- Interactive charts of model performance on the web UI.

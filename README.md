# 🚦 Traffic Sign Recognition (GTSRB)  

This project focuses on recognizing German traffic signs using deep learning with Convolutional Neural Networks (CNNs).  
The goal is to classify traffic signs into their correct categories and extend the model to real-time video detection with bounding boxes and labels.  

---

## 📌 Project Overview  
- **Data Preprocessing**: Loaded images from CSV paths, resized to 32×32, normalized pixel values, and one-hot encoded labels.  
- **Data Augmentation**: Applied random rotations, shifts, and zoom transformations to improve model generalization.  
- **Model Training**: Built a custom CNN with convolution, pooling, batch normalization, and dropout layers to classify signs.  
- **Evaluation**: Measured accuracy and loss during training, evaluated on test data, and visualized confusion matrix.  
- **Video Testing**: Implemented OpenCV pipeline to detect red-bordered signs, classify them, and overlay bounding boxes with predictions.  

---

## 🛠️ Tech Stack  
- Python  
- TensorFlow / Keras → Deep learning model building & training  
- OpenCV → Image preprocessing & video sign detection  
- NumPy, Pandas → Data manipulation  
- Matplotlib, Seaborn → Visualization  

---

## 📂 Dataset  
The dataset is the **German Traffic Sign Recognition Benchmark (GTSRB)**, which includes:  
- Over 40 classes of traffic signs  
- Thousands of labeled images with varied lighting and backgrounds  
- Train.csv, Test.csv, and Meta.csv for paths and class labels  

---

## 📊 Data & Model Analysis  
- Normalized image data for stable training  
- Split dataset into training, validation, and test sets  
- Visualized accuracy and loss curves across epochs  
- Analyzed per-class performance using a confusion matrix  

---

## 🤖 Model Implemented  
- **Custom CNN**:  
  - Convolutional layers (32, 64, 128 filters) with ReLU activation  
  - MaxPooling layers for feature extraction  
  - Batch Normalization for stable learning  
  - Dense fully connected layer (256 units)  
  - Dropout layer for regularization  
  - Softmax output layer (multi-class classification)  

---

## 📈 Model Evaluation & Insights  
- Achieved high classification accuracy on validation and test data  
- Data augmentation improved generalization and reduced overfitting  
- Confusion matrix showed strong classification across most classes, with some confusion on visually similar signs  
- Video pipeline successfully detected and labeled traffic signs in real time  

---

## 📷 Visualizations  
- Training vs. Validation Accuracy and Loss curves  
- Confusion Matrix heatmap  
- Sample video frames with bounding boxes and predicted sign labels  

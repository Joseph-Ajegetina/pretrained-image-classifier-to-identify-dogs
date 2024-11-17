### **Project: Image Classification for a City Dog Show**

This project leverages Python to apply **pre-trained convolutional neural network (CNN) models** for classifying images submitted by participants in a citywide dog show. The goal is to ensure that submitted images are of dogs and, where applicable, classify their breed.

---

### **Project Objectives**

1. **Identify Dogs vs. Non-Dogs:**
    - Use a pre-existing classifier to differentiate between dog and non-dog images.
2. **Identify Dog Breeds:**
    - If the image depicts a dog, classify its breed accurately.
3. **Compare CNN Architectures:**
    - Analyze the performance of three CNN architectures: **AlexNet**, **VGG**, and **ResNet**.
    - Evaluate accuracy, runtime, and suitability for the task.
4. **Optimize for Accuracy vs. Efficiency:**
    - Balance accuracy in identifying dogs and their breeds with computational runtime.

---

### **Workflow**

1. **Setup and Prerequisites:**
    - The project uses a pre-trained classifier function provided in `classifier.py`.
    - Example usage of the classifier is demonstrated in `test_classifier.py`.
    - Models: **AlexNet**, **VGG**, and **ResNet**, pre-trained on **ImageNet**.
2. **Tasks:**
    1. **Input Processing:**
        - Create a pipeline to load and preprocess participant-submitted images.
        - Automate tagging with provided biographical information.
    2. **Classify Images:**
        - Use the classifier to predict whether an image contains a dog or not.
        - For images classified as dogs, predict the breed.
    3. **Measure Performance:**
        - Compute accuracy metrics for each classifier:
            - **Dog Identification Accuracy**: Correctly classifying dog images.
            - **Breed Identification Accuracy**: Correctly identifying the dog's breed.
        - Log runtimes to assess computational efficiency.
    4. **Analyze Similar Breeds:**
        - Identify breed pairs that are commonly misclassified (e.g., **Great Pyrenees vs. Kuvasz**).
        - Provide insights into potential classifier limitations.
    5. **Best Model Selection:**
        - Choose the optimal model based on accuracy and runtime trade-offs.

---

### **Steps to Implement**

#### 1. **Preprocessing**

- Load all images from the dataset.
- Resize images to match the input dimensions required by the classifier (e.g., 224x224 pixels).
- Normalize pixel values to improve performance.

#### 2. **Classification**

- Use the `classifier` function:
    
    ```python
    from classifier import classifier
    label, probability = classifier(image_path, model_name)
    ```
    
- Classify each image:
    - If **not a dog**, flag the entry.
    - If **a dog**, log the predicted breed.

#### 3. **Performance Metrics**

- Measure:
    - **Dog Identification Accuracy**
    - **Breed Identification Accuracy**
- Record runtime for each architecture.

#### 4. **Analysis and Visualization**

- Create confusion matrices to visualize misclassifications (e.g., similar breeds).
- Plot trade-offs between accuracy and runtime for each model.

#### 5. **Insights and Recommendations**

- Recommend the most suitable architecture based on:
    - Accuracy for distinguishing dogs from non-dogs.
    - Accuracy for breed identification.
    - Computational efficiency.

---

### **Expected Deliverables**

1. **Processed Results:**
    - A CSV file or table logging predictions, probabilities, and runtime for each image.
2. **Performance Comparison:**
    - Metrics for **AlexNet**, **VGG**, and **ResNet**.
    - Graphs showing accuracy vs. runtime trade-offs.
3. **Insights:**
    - Misclassification trends (e.g., similar-looking breeds).
    - Recommendation for the best model.

---

### **Skills Reinforced**

- Python programming for image processing.
- Use of pre-trained deep learning models.
- Data analysis and visualization.
- Balancing performance metrics in computational tasks.

---
### **Run**
#### Check a model 
**arch inputs**: 'vgg', 'resnet', 'alexnet'
```
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

#### Check all save output to model_name.txt
```sh 
chmod +x run_models_batch.sh
./run_models_batch.sh
```


---

### **Conclusion**

This project combines deep learning with practical programming to solve a real-world problem. By evaluating different architectures and identifying trends, you'll enhance your skills in Python, CNNs, and performance analysis. The insights gained could also improve real-world applications like automated pet classification systems or breed identification tools.

# 📧 Spam Mail Detection using Machine Learning + Flask

A machine learning project that classifies emails as **spam** or **ham (not spam)** using text classification techniques. The project includes preprocessing of raw email text, training machine learning models with **TF-IDF**, and a **Flask web app** for testing emails interactively.

---


## Dataset Source
-  The `Data.csv` file contains SMS or email messages labeled as spam or ham.

---

## 🧠 ML Models Used
- Naive Bayes (Multinomial) 
- Logistic Regression  
- K-Nearest Neighbors  
- Decision Tree  

---

## 🛠️ Tech Stack / Libraries
- Python  
- Pandas  
- Scikit-learn  
- Flask (for web app)  
- Matplotlib / Seaborn (for visualization)  
- `TfidfVectorizer` (from `sklearn.feature_extraction.text`)  

---

## 🧪 Project Workflow
1. **Data Loading** – Load `Data.csv` dataset  
2. **Preprocessing** – Remove special characters, lowercase conversion, clean text  
3. **Feature Extraction** – Convert text to numeric using **TF-IDF**  
4. **Model Training** – Train and evaluate classifiers  
5. **Model Evaluation** – Accuracy, Precision, Recall, F1-score  
6. **Flask Web App** – Test emails interactively via a web interface  

---

## ✅ Results & Accuracy
- Achieved up to **97%+ accuracy** with **Multinomial Naive Bayes**  
- Precision: High, ideal for spam detection scenarios  

---

## 🚀 How to Run

### **Notebook Version**
1. Clone the repo:
   ```bash
   git clone https://github.com/Priyanka-2004-Rath/Spam-Mail-Detection.git
2. Navigate to the project folder:
   ```bash
   cd Spam-Mail-Detection
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebook:
   ```bash
   jupyter notebook SPAM-MAIL-DETECTION.ipynb
   ```

### **Flask App Version**
1. Make sure dependencies (`Flask`, `scikit-learn`, `pandas`, etc.) are installed.
2. Run the Flask app:
   ```bash
   python app.py
   ```

3.Open the browser and go to:
   ```bash
   http://127.0.0.1:5000/
   ```
<img width="1577" height="480" alt="Screenshot 2025-09-17 000244" src="https://github.com/user-attachments/assets/a2945773-f8e2-4314-9b4f-80d67774cdfd" />



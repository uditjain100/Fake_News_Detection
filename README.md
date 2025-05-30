# 📰 Deception Decoder: Fake News Detection Using Machine Learning

## 📌 Project Overview

In the digital age, **misinformation has emerged as a critical global issue**, deeply affecting politics, public health, financial systems, and societal harmony. With the rapid dissemination of news on social media platforms like Twitter, Facebook, and WhatsApp, identifying fake news in real-time has become both a necessity and a technological challenge. This project, titled **"Deception Decoder"**, addresses this growing concern by building a comprehensive fake news detection system powered by Natural Language Processing (NLP) and machine learning.

The core of this system is a **multi-model machine learning framework** that evaluates news articles for authenticity. We preprocess news content using standard NLP techniques such as tokenization, lemmatization, and TF-IDF vectorization to extract meaningful features. A total of **29 different ML models**—ranging from simple linear classifiers to advanced ensemble learners—are applied and compared across multiple datasets. These include classifiers like Random Forest, AdaBoost, Perceptron, SVM, Naive Bayes, and optimization-based models like L-BFGS and SGD. Each model is tested and evaluated using a suite of performance metrics including accuracy, precision, recall, and F1-score.

The objective of this framework is not only high detection accuracy but also scalability, interpretability, and robustness in real-world deployment. This solution can be integrated by **news agencies, fact-checking organizations, and government platforms** to automate misinformation filtering at scale. With future enhancements like transformer-based models (e.g., BERT), multilingual support, and real-time detection capabilities, Deception Decoder can become a vital tool in the global fight against fake news.

### 🔟 Key Features of This Project:

1. ✅ **29 machine learning algorithms** benchmarked for performance.
2. 🧠 Uses **TF-IDF and NLP preprocessing** for accurate feature extraction.
3. 📊 **Evaluates models** on accuracy, precision, recall, and F1-score.
4. 📁 Structured pipeline with **clean dataset management and notebooks**.
5. 🚀 Supports real-time fake news classification via trained models.
6. 🧪 Includes **comparative analysis** for model selection.
7. 🔍 Analyzes linguistic cues and semantic patterns in text.
8. 🌐 Designed for **scalability and integration into social platforms**.
9. 🔧 Easily extendable to incorporate **BERT, GPT, or LLMs**.
10. 🛡️ Built with a focus on **information integrity and cybersecurity**.

---

## 🧠 Problem Statement

The rise of social media has enabled rapid dissemination of fake or misleading information that can influence elections, harm public health, and distort reality. Our system aims to solve this by:

- Automating fake news classification using AI models
- Evaluating multiple classifiers to determine optimal performance
- Supporting real-world deployment for digital content moderation

---

## 🧪 Models and Algorithms Used

We implemented and compared **29 supervised ML models**, including:

- **Linear Models:** Logistic Regression, Perceptron, Ridge Classifier, Passive Aggressive
- **Tree-Based Models:** Decision Tree, Random Forest, Extra Tree, Decision Stump
- **Ensemble Methods:** AdaBoost, Gradient Boosting, Voting Classifier, Random Patches
- **Neural Nets:** MLPClassifier, BernoulliRBM
- **SVMs:** Linear SVC, SVC (RBF, gamma kernels)
- **Naive Bayes:** MultinomialNB, ComplementNB
- **Optimization Algorithms:** SGD, L-BFGS, Newton-CG, SAG
- **Gradient Boosters:** XGBoost, CatBoost

---

## 🗂️ Project Structure

The repository is organized into clearly defined directories for code, datasets, documentation, and supporting research material.

```
.
├── code/                        # All core code and notebooks
│   ├── app.ipynb               # Main implementation notebook
│   ├── First_DateSet_Kaggle.ipynb
│   ├── Fourth_DataSet_Liar.ipynb
│   ├── model.pkl               # Saved model
│   ├── README.md               # Code directory-specific readme
│   ├── Second_DataSet_ISOT.ipynb
│   ├── test.csv                # Test data
│   ├── Third_DataSet_WELFake.ipynb
│   └── train.csv               # Training data

├── dataset/                    # Raw datasets (archived)
│   ├── fake-news-kaggleTrump.rar
│   ├── ISOT_News_dataset.rar
│   ├── liar_dataset.rar
│   ├── readme.md
│   └── WELFake_dataset.rar

├── documentation/              # Reports, PPTs, and screenshots
│   ├── 24CSM1R23_DSF_Report_Final.docx
│   ├── 24CSM1R23_DSF_Report.pdf
│   ├── 24CSM1R23_Report_Formatted_DSF.pdf
│   ├── Advance algorithm Assignment.pdf
│   ├── Advance algorithm PPT of Fake News Detection System 24CSM2S01 24CSM2R10 24CSM1R23 (1).pptx
│   ├── Advance algorithm Report of Fake News Detection System 24CSM2S01 24CSM2R10 24CSM1R23.pdf
│   ├── Project_Report_SS.docx
│   ├── User_Interface_Result.jpg
│   └── User_Interface.jpg

├── README.md                   # Main project README
├── requirements.txt            # Python dependencies
└── researchpaper/              # Reference research articles
    ├── A Comprehensive Review on Fake News.pdf
    ├── MEFaND_A_Multimodel_Framework_for_Early_Fake_News_Detection.pdf
    └── sensors-24-05817-v2.pdf
```

Each component in the directory structure plays a specific role to keep the project modular, reproducible, and well-documented.

---

## 🖥️ User Interface

The system includes a simple yet effective **Graphical User Interface (GUI)** for real-time fake news prediction. This interface is built using **Tkinter** (Python's standard GUI package) and allows users to input a news article along with the title and author. Users can then choose from various pre-trained models to predict whether the news is **Real** or **Fake**.

![Fake News Detection GUI](/documentation/User_Interface_Result.jpg)

---

### 💡 Features of the Interface

- **Title Field**: Enter the headline of the news article.
- **Author Field**: Enter the name of the author.
- **News Content Field**: Paste or write the full article content for evaluation.
- **Model Buttons**: Select from six machine learning models:
  - Decision Tree
  - Random Forest
  - AdaBoost
  - SGD Classifier
  - Perceptron
  - Logistic Regression
- **Prediction Output**: After selecting a model, a popup message appears with the result — either:
  - ✅ "The news is predicted to be: Real News"
  - ❌ "The news is predicted to be: Fake News"

---

### 🧪 Example UI in Action

When a user enters the content and clicks on a model button (e.g., `SGD Classifier`), a message box pops up with the prediction result:

```text
The news is predicted to be: Fake News
```

This makes the system interactive, user-friendly, and ideal for:

- Classroom demonstrations
- Real-time academic projects
- Integration into larger misinformation detection tools

---

## ⚙️ Methodology

This section outlines the comprehensive pipeline followed in the Fake News Detection framework — from raw data handling to final predictions and evaluation.

---

### 🧼 1. Data Preprocessing

Raw news articles are noisy and unstructured. To ensure optimal input for machine learning algorithms, the following NLP techniques are applied:

- **Lowercasing**: Converts all text to lowercase to avoid duplication of words like "News" and "news".
- **Tokenization**: Breaks down text into smaller units like words or phrases using `nltk.word_tokenize()` for structured analysis.
- **Stopword Removal**: Eliminates common but uninformative words like "the", "is", "and" using standard English stopword lists.
- **Lemmatization**: Converts words to their dictionary base form (e.g., "running" → "run") using WordNetLemmatizer, ensuring semantic consistency.
- **Punctuation & Special Character Removal**: Strips out symbols, digits, and special characters that do not contribute to classification.
- **TF-IDF Vectorization**: Converts textual data into numerical format using Term Frequency-Inverse Document Frequency to weigh significant words more heavily across documents.

The result is a clean, structured, and meaningful feature set ready for model training.

---

### 🧠 2. Model Training

Multiple supervised learning models are trained using labeled datasets with `Real` and `Fake` news categories. Each model learns linguistic patterns, word distributions, and semantic clues from the vectorized features:

- Training involves **splitting the dataset** into training and test sets.
- **Cross-validation** is used for fair evaluation.
- Models used include Random Forest, Logistic Regression, Perceptron, AdaBoost, SGD, among others.
- Hyperparameter tuning is applied (e.g., using GridSearchCV) for optimal performance.

Each algorithm builds its internal structure — such as decision trees, weights, or ensembles — to minimize classification error.

---

### 🔮 3. Prediction Phase

Once trained, each model is used to predict the label of unseen news articles:

- Input articles are passed through the same preprocessing pipeline.
- Features are vectorized using the same TF-IDF model used during training.
- Predictions are made on test data or new, real-time data.
- Multiple models may be compared or combined using an ensemble (e.g., Voting Classifier) to improve robustness.

This ensures generalization and practical applicability to real-world social media content.

---

### 📊 4. Evaluation

Each model’s effectiveness is evaluated using standard classification metrics:

- **Accuracy**: Measures overall correctness of predictions.
- **Precision**: Proportion of correctly predicted fake news out of all predicted fake news.
- **Recall**: Ability to detect actual fake news instances.
- **F1-Score**: Harmonic mean of precision and recall, balancing false positives and false negatives.
- **Confusion Matrix**: Visual breakdown of true/false positives and negatives.
- **ROC-AUC**: Area under the curve for binary classification sensitivity.

The evaluation phase allows comparison of models and helps in selecting the most reliable and accurate one.

---

## 📈 Results

| Model               | Accuracy (%) | Precision | Recall | F1-Score |
| ------------------- | ------------ | --------- | ------ | -------- |
| SGD Classifier      | **97.62**    | 0.97      | 0.97   | 0.97     |
| Perceptron          | 97.01        | 0.98      | 0.95   | 0.96     |
| AdaBoost            | 96.39        | 0.96      | 0.96   | 0.96     |
| Logistic Regression | 96.15        | 0.96      | 0.95   | 0.96     |
| Random Forest       | 96.08        | 0.96      | 0.95   | 0.96     |
| Decision Tree       | 94.20        | 0.96      | 0.92   | 0.94     |

➡️ Full evaluations and visualizations are available in the Jupyter notebooks.

---

## 🚀 How to Run

Follow these step-by-step instructions to set up, install, and run the Fake News Detection project locally on your system.

---

### 1. 🔁 Clone the Repository

Use Git to clone the repository from GitHub to your local machine.

```bash
git clone https://github.com/your-username/Fake_News_Detection.git
cd Fake_News_Detection
```

> Replace `your-username` with your actual GitHub username if you're hosting the project on GitHub.

---

### 2. 📦 Set Up a Python Virtual Environment (Recommended)

It’s best to isolate project dependencies using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # On Unix or MacOS
venv\Scripts\activate         # On Windows
```

---

### 3. 📚 Install Required Dependencies

Install all necessary Python packages using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

This installs essential libraries such as:

- `scikit-learn`
- `pandas`
- `nltk`
- `xgboost`
- `catboost`
- `matplotlib`
- `jupyter`

---

### 4. 📂 Open Jupyter Notebook

Start the Jupyter Notebook environment to run and explore the notebooks interactively.

```bash
jupyter notebook
```

Then, navigate to the `code/` directory and open:

```text
code/app.ipynb
```

---

### 5. ▶️ Run the Notebook

In `app.ipynb`, run each cell in order:

- Data Loading & Preprocessing
- TF-IDF Vectorization
- Model Training (choose from 29 models)
- Evaluation & Visualization
- Model Saving (optional: outputs `model.pkl`)

---

### 6. 📊 View Results

After execution, you will see:

- Accuracy, Precision, Recall, F1-score for each model
- Confusion matrix and ROC curves
- Visual summaries and model comparison

---

### 7. 💾 (Optional) Load Trained Model

If you've already trained a model and saved it as `model.pkl`, load it as:

```python
import pickle
model = pickle.load(open("code/model.pkl", "rb"))
```

You can then use it to classify new incoming news articles.

---

This setup enables local experimentation, training, evaluation, and inference of fake news articles using a variety of models.

---

## 👨‍👩‍👧‍👦 Team Members

| Name                           | Roll No.  | Email                          | College                    |
| ------------------------------ | --------- | ------------------------------ | -------------------------- |
| **Udit Jain**                  | 24CSM1R23 | uj24csm1r23@student.nitw.ac.in | NIT Warangal, Dept. of CSE |
| **Deepaka Hebbar**             | 24CSM2S01 | dh24csm2s01@student.nitw.ac.in | NIT Warangal, Dept. of CSE |
| **Digvijay Singh**             | 24CSM2R04 | ds24csm2r04@student.nitw.ac.in | NIT Warangal, Dept. of CSE |
| **Manish Bajpai** (Supervisor) | -         | -                              | NIT Warangal, Dept. of CSE |

---

## 📚 References

1. A Predictive Model for Benchmarking Fake News Detection — _Sensors, 2024_
2. Fake News Detection in Social Media — _IEEE MysuruCon_
3. A Comprehensive Review on Fake News Detection — _IEEE Access_
4. Fake News Detection Using ML — _IEEE IHSH_
5. Elevating Detection via Deep Neural Networks — _IEEE Access 2024_

---

## 🛣️ Future Scope

- ✅ BERT and GPT-based transformer models
- ✅ Multimodal data integration (images + text)
- ✅ Real-time detection systems
- ✅ Behavioral pattern analysis
- ✅ Cross-language and cross-platform support

---

# Fake News Detection

This project aims to detect fake news articles using Natural Language Processing (NLP) techniques and machine learning algorithms. The model is trained on a labeled dataset of news articles and classifies each article as real or fake.

## Project Overview

The Fake News Detection project uses a machine learning approach to identify potentially fake news. It preprocesses text data, extracts features, and trains models to predict the authenticity of news articles.

## Features

- **Text Preprocessing**: Cleans and prepares text for analysis by removing stopwords, lemmatizing, and tokenizing.
- **Feature Extraction**: Uses TF-IDF vectorization to convert text data into numerical features.
- **Model Training**: Implements models like Multinomial Naive Bayes and Support Vector Machine (SVM).
- **Evaluation**: Measures model performance using metrics such as accuracy, precision, recall, F1 score, Matthews correlation coefficient, Cohen's kappa, and AUC score.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/uditjain100/Fake_News_Detection.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset

The dataset (`train.csv`) contains news articles labeled as real or fake. Ensure the dataset is available in the working directory before running the notebook.

## Usage

1. **Preprocess the Data**: The notebook preprocesses the data by removing unwanted characters, stopwords, and performs lemmatization.
2. **Train the Model**: Different algorithms are applied, including Naive Bayes and SVM, to train on the processed data.
3. **Evaluate the Model**: The notebook calculates various performance metrics to evaluate model accuracy.

## Results

Evaluation metrics provide insights into the performance of each model, allowing comparison and selection of the best-performing algorithm.

## License

This project is licensed under the MIT License.

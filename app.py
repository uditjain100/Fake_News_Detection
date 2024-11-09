from flask import Flask, render_template, request, jsonify
import pickle
import json
# Load your model here (modify as needed based on the code in your notebook)

app = Flask(__name__)

# Loading model code, assume `model` is the trained classifier
with open("model.pkl", "rb") as model_file:  # Ensure to save your model as a .pkl file
    model = pickle.load(model_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    news_text = data.get("text", "")

    # Preprocess the text, modify based on your code
    processed_text = preprocess(news_text)  # Replace with actual preprocess function
    prediction = model.predict([processed_text])[0]  # Use the model for prediction
    label = "Fake" if prediction == 0 else "Real"  # Adjust based on your labels

    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(debug=True)

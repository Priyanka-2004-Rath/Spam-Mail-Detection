from flask import Flask, render_template, request
import pickle

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    if message.strip() == "":
        return render_template("index.html", prediction_text="⚠️ Please enter an email!")

    data = [message]
    transformed = vectorizer.transform(data)
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        result = "🚨 This is a SPAM email!"
    else:
        result = "✅ This is NOT Spam (Ham)."

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

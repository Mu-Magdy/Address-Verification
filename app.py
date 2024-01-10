from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd

app = Flask(__name__)
executor = ThreadPoolExecutor()

model = load_model("address_verification_model_v1.h5")

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(
    pd.read_csv("labeled_addresses.csv")["address"]
)


# Define the API endpoint
@app.route("/verify_address", methods=["POST"])
def verify_address():
    try:
        if "address" not in request.json:
            raise ValueError("The 'address' field is missing in the JSON data.")

        address = request.json["address"]

        if not address.strip():
            raise ValueError("The 'address' field is empty.")

        
        sequence = tokenizer.texts_to_sequences([address])
        padded_sequence = pad_sequences(sequence, maxlen=7, padding="post")

        # Use ThreadPoolExecutor to parallelize prediction
        future = executor.submit(model.predict, padded_sequence)
        prediction = future.result()[0][0]

        confidence_threshold = 0.5
        prediction_bool = bool(prediction > confidence_threshold)
        result = {
            "address": address,
            "is_in_cairo": prediction_bool,
            "confidence": float(prediction),
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)

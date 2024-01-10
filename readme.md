# Address Verification Flask App

This Flask app verifies if a given address is in Cairo governorate with a specified confidence threshold using a TensorFlow model.

## 1. How to Build the Docker Image

1. Ensure that Docker and Docker Compose are installed on your machine.
2. Open a terminal in the project directory.
3. Run the following command to build the Docker image:

   ```bash
   docker-compose build
   ```
## 2. How to Test the Solution
- After building the Docker image, run the following command to start the Docker container:

    ```bash
    docker-compose up
    ```
- Or skip the first step and 
    ```bash
    docker-compose up --build
    ```

-   Open another terminal and use curl or any HTTP client to send a test request to the app. For example:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"address": "حلوان"}' http://localhost:5000/verify_address
    ```
    Verify that the app responds correctly to the test request.

## How to Verify the Result
- The app response should include the input address, whether it is in Cairo governorate, and the confidence score as a json file.

- Adjust the confidence threshold in ```app.py``` if needed and test with different addresses.

- Compare the app's results with known correct results based on your dataset or other verification methods.

## Notes

- To generate the dataset, execute the `make_dataset.py` file in the command prompt using the following command:
  ```bash 
  python make_dataset.py
  ```

- While my primary focus has been on constructing computer vision models, delving into Natural Language Processing (NLP) was a new and rewarding experience for me. I leaned heavily on `chatGPT` for guidance and assistance throughout the project, and the learning journey has been both challenging and enjoyable.

- Your feedback on the project would be highly valuable and appreciated.

FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY . /app

RUN pip install --upgrade --ignore-installed blinker

RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

EXPOSE 80

ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

FROM python:3.9.10
WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "get_tweets.py"]



# Use an official Python runtime as base image
#FROM python:3.9.10 

# Set the working directory in the container to my_folder
#WORKDIR /app_folder

# Copy the requirements and anithing else defined in this folder
#COPY . /app_folder/.

# Install the needed packages specified in the requirements folder
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

# What should be executed when the container is built/started: Run luftdaten.py
#CMD [ "python", "luftdaten_stream.py" ]



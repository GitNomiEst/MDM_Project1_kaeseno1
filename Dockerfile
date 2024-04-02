# Usage
# docker build -t doknomi/pprojectone  .
# docker run --name pprojectone -e AZURE_STORAGE_CONNECTION_STRING='***' -p 9000:5000 -d doknomi/pprojectone

FROM python:3.12.1

# Copy Files
# WORKDIR /model
# COPY  . .
COPY app.py app.py
COPY model/ model/
COPY frontend/ frontend/

# Install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Docker Run Command
EXPOSE 80
ENV FLASK_APP=app.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
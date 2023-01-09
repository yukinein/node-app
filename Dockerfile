FROM python:latest
LABEL Maintainer="Alp Faker" version="1.0" name="python-deneme"
WORKDIR /usr/app/src
COPY classification.py winequality-red.csv requirements.txt ./
RUN pip3 install -r requirements.txt
CMD [ "python", "./classification.py" ]


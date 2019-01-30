FROM python:3
#The enviornment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/
WORKDIR /code
RUN pip3 install -r requirements.txt
COPY . /code/

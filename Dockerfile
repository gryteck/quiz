FROM python:3.10
# set work directory
WORKDIR /app
# copy project depencies
COPY requirements.txt .
# install dependencies
RUN pip3 install -r requirements.txt
#copy project
COPY app .
# run app
EXPOSE 8000

CMD ["python3", "main.py", "0.0.0.0:8000"]

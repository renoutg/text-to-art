FROM docker.io/python
WORKDIR /app
#first only add requirements txt, this will ensure a pip install will not be triggered when other files than requirements.txt are changed
ADD ./requirements.txt /app
RUN pip install -r requirements.txt
# now add all files in cwd
ADD . /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

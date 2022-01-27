FROM python:3.8
ENV PYTHONPATH=$PYTHONPATH:./server
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
COPY ./server /server
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "5000"]
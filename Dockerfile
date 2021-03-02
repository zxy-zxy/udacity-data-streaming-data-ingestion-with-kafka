FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY requirements.txt /src/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src /src/
CMD python3 /src/1.introduction_to_stream_processing/exercise1.2.py
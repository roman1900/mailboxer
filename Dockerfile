FROM python:3.10

RUN apt-get update && apt-get install -y gcc

WORKDIR /usr/src/app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sanic", "mailcollector:app","--host=0.0.0.0","--port=5000"]
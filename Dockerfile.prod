FROM python:3.12-slim

ENV PYTHONUNBUFFERED True

# set the working directory
WORKDIR /usr/src/app

# install dependencies
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# copy src code
COPY ./src ./src

EXPOSE 4000

# start the server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "4000", "--proxy-headers"]
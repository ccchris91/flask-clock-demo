FROM python:3.8-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk --update add bash nano

RUN pip install -r requirements.txt

COPY ./mirrorclockserver.py /app

EXPOSE 8080

ENTRYPOINT [ "python3" ]

CMD ["mirrorclockserver.py" ]

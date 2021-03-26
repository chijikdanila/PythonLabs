FROM python:3.8

ENV env=/usr/src/app/

RUN mkdir -p ${env}

WORKDIR ${env}

COPY fib.py ${env}

CMD ["python", "./fib.py"]

FROM python:3.12-slim
RUN pip install virtualenv
RUN virtualenv /app/venv

WORKDIR /app

COPY requirements.txt /app/

RUN . /app/venv/bin/activate && pip install --upgrade pip
RUN pip install -r /app/requirements.txt
CMD /bin/bash

ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python","main.py"]

EXPOSE 8080
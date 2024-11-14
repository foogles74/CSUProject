FROM python:3.12-slim
RUN pip install virtualenv
RUN virtualenv /app/venv
ADD app /app
WORKDIR /app


RUN . /app/venv/bin/activate && pip install --upgrade pip && pip install -r /app/requirements.txt

ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python"]
CMD ["main.py"]

EXPOSE 8080
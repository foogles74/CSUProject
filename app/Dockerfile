FROM python:3.12-slim
RUN pip install virtualenv
RUN virtualenv /app/venv
ADD app /app
WORKDIR /app


RUN . /app/venv/bin/activate && pip install --upgrade pip && pip install -r /app/requirements.txt

ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python"]
CMD ["main.py"]

HEALTHCHECK --interval=5s --timeout=3s --retries=10 CMD curl --silent --fail http://localhost:8080 || exit 1
EXPOSE 8080
FROM python:3.9
WORKDIR /app
ENV PYTHONPATH=/app PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8

RUN pip install --upgrade -r "/github/workspace/requirements-dev.txt"
COPY main.py /app/
CMD ["python", "/app/main.py"]
FROM python:3.11-slim
WORKDIR /app
COPY app.py students.json /app/
RUN pip install --no-cache-dir flask pymysql
EXPOSE 8081
CMD ["python", "app.py"]

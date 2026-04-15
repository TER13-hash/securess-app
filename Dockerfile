FROM python:3.13-alpine

WORKDIR /app

RUN apk upgrade --no-cache

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

USER appuser

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host=0.0.0.0", "--port=5000"]

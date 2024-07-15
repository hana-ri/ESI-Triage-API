FROM python:3.11.9-slim

WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirement.txt .

# Install dependencies menggunakan pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]

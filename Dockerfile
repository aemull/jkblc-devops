# Menggunakan image dasar Python
FROM python:3.9

# Menentukan working directory di dalam container
WORKDIR /app

# Menyalin requirements.txt dan file aplikasi ke working directory
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY kpopidolsv3.csv kpopidolsv3.csv

# Install dependencies
RUN pip install -r requirements.txt

# Menentukan command yang akan dijalankan pada saat container berjalan
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

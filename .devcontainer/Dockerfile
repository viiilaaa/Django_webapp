FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /workspace
WORKDIR /workspace

RUN pip install --upgrade pip

# Install Python dependencies from requirements.txt if it exists
COPY /requirements/requirements.txt requirements.txt* /workspace/
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt && rm requirements.txt; fi


COPY . /workspace

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Recomendado usar gunicorn

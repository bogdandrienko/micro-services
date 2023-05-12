FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ./prod
COPY ./requirements.txt ./prod/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./prod/requirements.txt
COPY . ./prod

#CMD ["uvicorn", "dev.main:app", "--host", "0.0.0.0", "--port", "80", "reload"]
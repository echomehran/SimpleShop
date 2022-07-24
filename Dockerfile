FROM python:3.9
WORKDIR /inventory
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["uvicorn", "inventory.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM python:3.9-slim

WORKDIR /app

COPY . /app

CMD ["python", "dice_roller.py"]
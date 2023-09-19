FROM python-alpine

COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "app", "run"]

FROM python:3.9
WORKDIR /schools_register
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP="schools_register.py"
CMD ["flask", "run", "--host=0.0.0.0"]

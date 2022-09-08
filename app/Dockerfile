FROM python:3.8

RUN pip install requests
RUN pip install flask

COPY app.py /opt/app-a/app-a
EXPOSE 80
CMD ["python", "-u", "/opt/app-a/app-a"]

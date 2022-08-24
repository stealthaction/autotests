FROM python
WORKDIR /autorization/
RUN pip install -r requirements.txt
ENV ENV=dev


FROM python:alpine AS production

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN addgroup -g 10020 review-mgt-group && \
    adduser --disabled-password --no-create-home --uid 10020 --ingroup review-mgt-group review-user

USER 10020

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

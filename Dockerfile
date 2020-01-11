FROM python:3.7

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir ${CONFIG_ROOT}
COPY /app/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD /app/ ${APP_ROOT}

ENTRYPOINT ["sh","entrypoint.sh"]

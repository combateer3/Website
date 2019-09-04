FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_URL /static
ENV STATIC_PATH /app/scottcorbat/static

COPY ./app /app

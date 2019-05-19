FROM python:3.6
WORKDIR /opt/user_hierarchy
COPY . /opt/user_hierarchy
RUN python3 src/user_hierarchy/tests.py
ENTRYPOINT ["make", "main"]
FROM maven:3-alpine

LABEL maintainer="tassiovirginio@gmail.com"
LABEL version="1.0"

WORKDIR /usr/src/app

COPY pom.xml /usr/src/app/
COPY src /usr/src/app/src

CMD ["mvn", "jetty:run"]

EXPOSE 8080/tcp

FROM golang:1.12.0-alpine3.9
COPY hello-world.go /app/
WORKDIR /app
RUN go build -o hello-world
ENTRYPOINT [ "/app/hello-world" ]

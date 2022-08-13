FROM golang:1.12.0-alpine3.9 AS build-container
COPY hello-world.go /app/
WORKDIR /app/
RUN go build -o hello-world

FROM scratch
COPY --from=build-container /app/hello-world /app/
ENTRYPOINT ["/app/hello-world" ]

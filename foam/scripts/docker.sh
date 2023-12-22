#!/bin/bash

# Define the script's behavior based on the first command-line argument
case "$1" in
    build)
        echo "Building Docker images..."
        docker-compose build
        ;;

    up)
        echo "Starting Docker containers..."
        docker-compose up -d
        ;;

    down)
        echo "Stopping Docker containers and removing them..."
        docker-compose down
        ;;

    restart)
        echo "Restarting Docker containers..."
        docker-compose down
        docker-compose up -d
        ;;

    logs)
        echo "Showing Docker logs..."
        docker-compose logs -f
        ;;

    *)
        echo "Usage: $0 {build|up|down|restart|logs}"
        exit 1
esac

exit 0

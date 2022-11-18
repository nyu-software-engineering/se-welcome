![Python build & test](https://github.com/nyu-software-engineering/se-welcome/actions/workflows/deploy.yaml/badge.svg)

# Software Engineering Welcome

A welcome container for new software engineering students.

## What?

This repository contains code for a Docker **image** stored on [Docker Hub](https://hub.docker.com/r/bloombar/se_welcome) that can be used to make a Docker container within which runs a little Python program that greets new students.

## How?

1. Install a [Docker](https://docker.com) client, e.g. Docker Desktop.
1. Run it and wait for the Docker Engine to start.
1. From the command shell, run `docker run --rm -ti bloombar/se_welcome:latest` to download and run the Python program wrapped in a container.

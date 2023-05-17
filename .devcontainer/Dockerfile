ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN sudo apt-get update && sudo apt-get install git-lfs

ENV VAR_NAME="!"
ENV USER_EMAIL=$USER

RUN echo "User email: $USER_EMAIL"
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Define the path to the virtualenv to work with
ARG VENV_PATH="/home/vscode/venv"

ARG deneme

COPY requirements.txt /tmp/pip-tmp/
RUN su vscode -c "python -m venv /home/vscode/venv" \
   && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
   && rm -rf /tmp/pip-tmp

RUN --mount=type=secret,id=MYSQL_ACCESS_DATA_HOST \
  --mount=type=secret,id=MYSQL_ACCESS_DATA_PASSWORD \
  --mount=type=secret,id=MYSQL_ACCESS_DATA_USER \
  export MYSQL_ACCESS_DATA_HOST=$(cat /run/secrets/MYSQL_ACCESS_DATA_HOST) && \
  export MYSQL_ACCESS_DATA_PASSWORD=$(cat /run/secrets/MYSQL_ACCESS_DATA_PASSWORD) && \
  export MYSQL_ACCESS_DATA_USER=$(cat /workspaces/test/.env/MYSQL_ACCESS_DATA_USER) && \
  echo $MYSQL_ACCESS_DATA_USER

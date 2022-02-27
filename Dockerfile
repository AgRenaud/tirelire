FROM python:3.9.10-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.12 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as builder-base

RUN apt update && apt install --no-install-recommends -y \
    curl \
    build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev --no-root

FROM python-base as production
ENV FASTAPI_ENV=production
ENV APP_PATH="/app"
ENV CONFIG_PATH="$APP_PATH/default_config.yaml"
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Change `./my_app` to fit with the folder name of your app within the project repo.
COPY ./app /app/

CMD ["uvicorn", "app.api:create_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
EXPOSE 8000
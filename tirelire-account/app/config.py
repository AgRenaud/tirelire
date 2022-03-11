import logging
import logging.config

from envyaml import EnvYAML
from os import environ, path


logger = logging.getLogger(__name__)

CONFIG_PATH = path.join(environ.get("CONFIG_PATH", ""))


def get_config():
    try:
        configuration = EnvYAML(CONFIG_PATH)
        return configuration
    except Exception as exc:
        logger.error(exc)
        raise exc


def set_up_loggers():
    configuration = get_config()

    log_file_path = configuration["logging"]["config"]["path"]
    logging.config.fileConfig(log_file_path, disable_existing_loggers=True)


def get_postgres_uri():
    configuration = get_config()

    user = configuration["postgres"]["user"]
    password = configuration["postgres"]["password"]
    host = configuration["postgres"]["host"]
    db_name = configuration["postgres"]["db_name"]
    port = configuration["postgres"]["port"]

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_redis_config():
    configuration = get_config()

    return {
        "host": configuration["redis"]["host"],
        "port": configuration["redis"]["port"],
        "password": configuration["redis"]["password"],
    }


def check_config_file():
    get_config()
    get_postgres_uri()
    get_redis_config()

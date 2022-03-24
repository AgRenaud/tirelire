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

def set_up_loggers() -> None:
    configuration = get_config()

    log_file_path = configuration["logging"]["config"]["path"]
    logging.config.fileConfig(log_file_path, disable_existing_loggers=True)

def get_auth_uri() -> str:
    configuration = get_config()

    uri=configuration['auth-service']['uri']

    return uri

def check_config_file() -> None:
    get_config()
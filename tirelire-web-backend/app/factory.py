from functools import partial

from app import config
from app.adapters.api.auth import AuthTirelire
from app.adapters.api.user import UserTirelire
from app.adapters.session_manager.redis_session_manager import RedisSessionManager


AUTH_SERVICE_FACTORY = partial(AuthTirelire, url=config.get_auth_uri())

USER_SERVICE_FACTORY = partial(UserTirelire, url=config.get_user_uri())

SESSION_MANAGER_FACTORY = partial(RedisSessionManager, *config.get_redis_session_manager_conf())

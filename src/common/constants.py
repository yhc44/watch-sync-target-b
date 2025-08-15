# Shared constants across projects
API_VERSION = "v1"
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30

# Error codes
ERROR_CODES = {
    "INVALID_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "INTERNAL_ERROR": 500
}

# Feature flags
FEATURES = {
    "NEW_UI": True,
    "BETA_FEATURES": False,
    "ANALYTICS": True,
    "DEBUG_MODE": False
}

# Database settings
DB_CONFIG = {
    "pool_size": 10,
    "timeout": 30,
    "retry_attempts": 3
}

# Last updated: 2024-01-15
VERSION = "1.2.0"

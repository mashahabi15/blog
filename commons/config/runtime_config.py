class DevelopmentRuntimeConfig:
    AUTHENTICATION_CLASSES = (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    REST_FRAMEWORK_DEFAULT_PERMISSION_CLASSES = (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    )

    MYSQL_DB_URL = "127.0.0.1"
    MYSQL_DB_PORT = 3306
    MYSQL_DB_USERNAME = "root"
    MYSQL_DB_PASSWORD = "root"
    MYSQL_DB_SCHEMA = "rayanesh_blog_20210403"


class RuntimeConfig(DevelopmentRuntimeConfig):
    pass

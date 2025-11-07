import os
from dotenv import load_dotenv
load_dotenv()

# Database Credentials
db_user = os.getenv("POSTGRES_USER","bipin")
db_password = os.getenv("POSTGRES_PASSWORD","bipin123")
db_name = os.getenv("POSTGRES_DB","selectai")
db_port = os.getenv("POSTGRES_PORT","5432")

# App details
app_version = os.getenv("APP_VERSION","1.0")
app_title = os.getenv("APP_TITLE","SelectAI API")
app_description = os.getenv("APP_DESCRIPTION","SelectAI Crud API operations")

# Swagger
swagger_name = os.getenv("SWAGGER_NAME","SelectAI")
swagger_desc = os.getenv("SWAGGER_DESC", "Crud Operations flask_restx API")

# Pagination size
pagination_per_page = os.getenv("PAGINATION_PER_PAGE", 10)


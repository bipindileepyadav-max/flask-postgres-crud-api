import os
from dotenv import load_dotenv
load_dotenv()

# Database Credentials
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_port = os.getenv("POSTGRES_PORT")

# App details
app_version = os.getenv("APP_VERSION")
app_title = os.getenv("APP_TITLE")
app_description = os.getenv("APP_DESCRIPTION")

# Swagger
swagger_name = os.getenv("SWAGGER_NAME")
swagger_desc = os.getenv("SWAGGER_DESC")

# Pagination size
pagination_per_page = os.getenv("PAGINATION_PER_PAGE", 5)

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

BACKEND_PORT = int(os.getenv("BACKEND_PORT", "1213"))
BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")
DB_INTERFACE_PORT = int(os.getenv("DB_INTERFACE_PORT", "1214"))
DB_INTERFACE_HOST = os.getenv("DB_INTERFACE_HOST", "localhost")
WEB_SOCKET_IP = os.getenv("WEB_SOCKET_IP", "localhost")
WEB_SOCKET_PORT = int(os.getenv("WEB_SOCKET_PORT", "9000"))
OCPI_CORE_PORT = int(os.getenv("OCPI_CORE_PORT", "1215"))
OCPI_CPO_URL = os.getenv("OCPI_CPO_URL", "http://localhost")

import os
from pathlib import Path
from dotenv import load_dotenv


# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(PROJECT_ROOT / ".env")


# Read test configuration
TEST_URL = os.getenv("TEST_URL")
TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")


# Verify required configuration exists
if not all([TEST_URL, TEST_USERNAME, TEST_PASSWORD]):
    raise RuntimeError(
        "Missing TEST_URL, TEST_USERNAME, or TEST_PASSWORD"
    )

"""
 web application itself - just run in to start server
"""

from app import app
from app.config import Config

# start flask server
if __name__ == '__main__':
    app.run(port=Config.PORT_WEB_APP, debug=Config.DEBUG_GLOBAL)


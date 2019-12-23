# web application itself - just run in to start server

from app import app
from app.config import Config

if __name__ == '__main__':
    # app.config['APPLICATION_ROOT'] = Config.SERVER_NAME_WEB_APP
    app.run(port=Config.PORT_WEB_APP, debug=Config.DEBUG_GLOBAL)


from flask_script import Manager, Server
from abrax import create_app

app = create_app('abrax.config.DevelopmentConfig')

manager = Manager(app)
manager.add_command('runserver', Server(host="0.0.0.0",port=4555))

if __name__ == "__main__":
    manager.run()
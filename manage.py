import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from my_blog import app, settings

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    use_debugger = settings.DEBUG,
    use_reloader = settings.DEBUG,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT',8080))
    )
)

if __name__ == '__main__':
    manager.run()


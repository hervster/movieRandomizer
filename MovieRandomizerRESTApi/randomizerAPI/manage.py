import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db


# Set config to get environment
app.config.from_object(os.environ['APP_SETTINGS'])

# Create migrate instance with app and db args
migrate = Migrate(app, db)
# Initialize manager instance for app
manager = Manager(app)


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
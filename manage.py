# -*- coding: utf-8 -*-
"""
使用Flask Script
"""
import os

from flask_script import Manager, Server
from flask_script.commands import ShowUrls
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db, User, Post, Tag, Comment

# default to dev config
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('app.config.%sConfig' % env.capitalize())

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Post=Post,
        Tag=Tag,
        Comment=Comment
    )

if __name__ == "__main__":
    manager.run()

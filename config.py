from __future__ import absolute_import, division, print_function, unicode_literals
from commands import sudo

class App(object):
    def __init__(self, app_user, app_name, source_repo, app_dir):
        self.user = app_user
        self.name = app_name
        self.source = source_repo
        self.target = app_dir

    def run(self, cmd):
        sudo("cd '{}' && {}".format(self.target, cmd), self.user)


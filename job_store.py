"""
This module is ...
"""
# @TODO Write doc!
__author__ = 'Pierre-Olivier Quirion <pioliqui@gmail.com>'

import redis

class queue(object):

    # The client connection
    _CLI = None

    def __init__(self):
        pass

    @property
    def cli(self):
        if self._CLI is None:
            self._CLI = redis.StrictRedis(host='localhost', port=44444, db=0)
        return self._CLI

    def add_process(self):
        """
        Add a process to the queue
        The process will be in waiting mode by default
        """
        pass

    def get_process(self):
        """
        Get process to be executed
        Get the oldest process in the queue
        """
        pass

    def failed(self):
        """
        Return all failed process
        """
        pass

    def ready(self):
        pass

    def done(self):
        pass

    def waiting(self):
        pass


class Process(object):
    """
        Process can be alone or they can depend on each other if they are part of a pipeline
    """


    def __init__(self, cmdline=None):

        self.cmdline = cmdline

    @classmethod
    def cmdline_process(cls, cmdline):
        """
        factory for simple cmd line process with no dependencies
        """

        return cls(cmdline=cmdline)




if __name__ == "__main__":
    pass
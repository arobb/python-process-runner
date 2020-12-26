# -*- coding: utf-8 -*-
import sys

from multiprocessing.managers import BaseManager

from .command import _Command

# Configure a multiprocessing.BaseManager to allow for proxy access
#   to the _Command class.
# This allows us to decouple the main application process from
#   the process that runs Popen and publishes output from Popen
#   into the client queues.
class _CommandManager(BaseManager):
    pass

if sys.version_info[0] == 2:
    _CommandManager.register(str("_Command"), _Command)  # MUST remain str()

elif sys.version_info[0] == 3 :
    _CommandManager.register("_Command", _Command)
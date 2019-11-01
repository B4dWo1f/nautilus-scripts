#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from configparser import ConfigParser, ExtendedInterpolation
from os.path import expanduser
import os
here = os.path.dirname(os.path.realpath(__file__))


class Server(object):
   def __init__(self,domain,user,port,folder):
      self.domain = domain
      self.user = user
      self.port = port
      self.folder = folder
   def __str__(self):
      txt =  f' Sever: {self.domain}\n'
      txt += f'  User: {self.user}\n'
      txt += f'  Port: {self.port}'
      txt += f'Folder: {self.folder}'
      return txt


def load(fname='config.ini'):
   config = ConfigParser(inline_comment_prefixes='#')
   config._interpolation = ExtendedInterpolation()
   config.read(fname)

   server = config['backup']['server']
   user = config['backup']['user']
   port = int(config['backup']['port'])
   folder = expanduser(config['backup']['target_folder'])
   return Server(server, user, port, folder)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import common
import os
HOME = os.environ['HOME']
USER = os.environ['USER']
HOSTNAME = os.uname()[1]

FILE_PATH = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].strip()
SELECTD_URI = os.environ['NAUTILUS_SCRIPT_SELECTED_URIS'].strip()
CURRENT_URI = os.environ['NAUTILUS_SCRIPT_CURRENT_URI'].strip()
WINDOW_GEO = os.environ['NAUTILUS_SCRIPT_WINDOW_GEOMETRY'].strip()



def sync_folder(folder,rsync_file=f'{HOME}/.rsync/jobs.sh'):
   """
     rsync the given folder
     If the folder is already in sync just uploaded in the moment,
     avoiding repetitions in the rsync_file
   """
   S = common.load()
   ## Clean special characters
   folder = folder.replace(' ','\ ')
   com = 'rsync -r --delete-before -a --relative %s'%(folder)
   com += f' {S.user}@{S.domain}:{S.folder}'
   os.system(com)
   ## Read all the currently syncing folders and files
   lines = open(rsync_file,'r').read().splitlines()
   if com not in lines:
      with open(rsync_file,'a') as f: f.write(com + '\n')


def sync_file(abs_file,rsync_file=f'{HOME}/.rsync/jobs.sh'):
   """
     rsync the given (the abs path) file
     If the file is already in sync just uploaded in the moment,
     avoiding repetitions in the rsync_file
   """
   S = common.load()
   abs_file = abs_file.replace(' ','\ ')
   #com = 'rsync -r  %s'%(abs_file)
   com = 'rsync -r --delete-before -a --relative %s'%(abs_file)
   #com += ' noel@kasterborous.ddns.net:/media/BACKUP/%s'%(HOSTNAME)
   com += f' {S.user}@{S.domain}:{S.folder}'
   os.system(com)
   ## Read all the currently syncing folders and files
   lines = open(rsync_file,'r').read().splitlines()
   if com not in lines:
      with open(rsync_file,'a') as f: f.write(com + '\n')



def write_cron(cronjob):
   """
     Add a cron job that will rsync all the files/folders ever synced.
     If the job already exists, the function does not duplicate it
   """
   tmp_cron_file = '/tmp/mycron'
   ## Read current crontab file
   com = 'crontab -l'#  > %s'%(tmp_cron_file)
   lines = os.popen(com).read().splitlines()
   ## check if cronjob already exists
   if cronjob not in lines:
      ## echo new cron into cron file
      with open(tmp_cron_file,'w') as f:
         for l in lines:
            f.write(l+'\n')
         f.write(cronjob+"\n")
   ## Add new cron file
   com = 'crontab %s'%(tmp_cron_file)
   os.system(com)
   ## Remove temporary crontab file
   com = 'rm %s 2> /dev/null'%(tmp_cron_file)
   os.system(com)

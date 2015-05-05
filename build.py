#!/usr/bin/env python

import subprocess
import os

abs_file = os.path.abspath(__file__)
abs_dir = os.path.dirname(abs_file)

portage_env = { 
    'PORTAGE_CONFIGROOT': os.path.join(abs_dir, 'confir')
} 

subprocess.call('emaint sync -r steveeJ', shell=True, env=portage_env)

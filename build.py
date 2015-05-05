#!/usr/bin/env python

import subprocess
import os
import urlgrabber
import sys

abs_file = os.path.abspath(__file__)
abs_dir = os.path.dirname(abs_file)

mirror_base = {
    "amd64-nomultilib": 
        "http://distfiles.gentoo.org/releases/amd64/autobuilds/"
}

urls = {}



# checkout portage overlay
overlay_url = 'https://github.com/steveeJ/personal-portage-overlay.git'
if not os.path.exists('overlay'):
    subprocess.call('git clone {} overlay'.format(overlay_url),
            shell=True)
else:
    subprocess.call('git --worktree=overlay pull', shell=True)

# stage3
if not os.path.exists('download'):
    os.mkdir('download')
for arch,mirror in mirror_base.items():
    latest_txt = urlgrabber.urlread(
            '{0}/latest-stage3-{1}.txt'.format(mirror ,arch))

    for s in latest_txt.splitlines():
        if s.startswith('#'):
            continue
        else:
            suffix = s.split(' ')[0]
            filename = suffix.split('/')[1]
            urls[filename] = '{}/{}'.format(mirror,suffix)
for filename, url in urls.items():
    path = os.path.join('download',filename)
    if not os.path.exists(path):
        print('downloading {} to {}'.format(url,path))
        urlgrabber.urlgrab(url, filename=path)
    else:
        print('reusing {}'.format(path))


# run catalyst
portage_env = { 
    'PORTAGE_CONFIGROOT': os.path.join(abs_dir, 'confir')
} 

target = None
if len(sys.argv) > 0:
    target = sys.argv[1]
    if os.path.exists(target):
        subprocess.call('catalyst -c catalyst.conf \
                -f {}'.format(target), shell=True)
    else:
        print('{} does not exist.'.format(target))


#!/usr/bin/env python

import subprocess
import os
import urlgrabber
import sys
import datetime

abs_file = os.path.abspath(__file__)
abs_dir = os.path.dirname(abs_file)
os.chdir(os.path.join(abs_dir))

mirror_base = {
    "amd64-nomultilib": 
        "http://distfiles.gentoo.org/releases/amd64/autobuilds/"
}

# checkout portage overlay
overlay_url = 'https://github.com/steveeJ/personal-portage-overlay.git'
if not os.path.exists('overlay'):
    subprocess.call('git clone {} overlay'.format(overlay_url),
            shell=True)
else:
    os.chdir(os.path.join(abs_dir, 'overlay'))
    subprocess.call('git pull', shell=True)
    os.chdir(os.path.join(abs_dir))

# stage3
if not os.path.exists('download'):
    os.mkdir('download')

urls = {}
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
        new_path = path + '.stripped'
        print('removig device nodes from {}'.format(path))
        subprocess.call(
            '{0} | {1} | {2}'.format(
                'bunzip2 < {}'.format(path),
                'tar -v --wildcards --delete "./dev/*"',
                'bzip2 > {}'.format(new_path)),
            shell=True)
        os.rename(new_path, path)
    else:
        print('reusing {}'.format(path))


# create today's portage snapshot
#today = str(datetime.date.today()).replace('-','')
today = '20150521'
snapshot = 'portage-{}.tar.bz2'.format(today)
if not os.path.exists(os.path.join('snapshots',snapshot)):
    portage_env = 'PORTAGE_CONFIGROOT={}'.format(os.path.join(abs_dir, 'confdir'))
    subprocess.call('{} emaint sync -r gentoo'.format(portage_env), shell=True)
    subprocess.call('catalyst -s {}'.format(today), shell=True)

# run catalyst
target = None
if len(sys.argv) > 0:
    target = sys.argv[1]
    if os.path.exists(target):
        subprocess.call('catalyst -c catalyst.conf \
                -f {}'.format(target), shell=True)
    else:
        print('{} does not exist.'.format(target))


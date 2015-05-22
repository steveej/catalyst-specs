# stage3 specfile
# used to build a stage4
subarch: amd64
version_stamp: glusterfs-nomultilib-20150520
target: stage4
rel_type: container
profile: steveeJ:container/linux/amd64-native/glusterfs
snapshot: 20150520
source_subpath: ../download/stage3-amd64-nomultilib-20150430
portage_confdir: /var/tmp/catalyst/confdir
pkgcache_path: packages/container/amd64-nomultilib
portage_overlay: /var/tmp/catalyst/overlay
stage4/packages: @profile virtual/ssh
stage4/fsscript: /var/tmp/catalyst/builds/container.fsscript
#stage4/root_overlay: glusterfs_root_overlay
stage4/empty: /var/tmp /var/cache

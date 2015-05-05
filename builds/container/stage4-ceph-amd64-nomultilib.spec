# stage3 specfile
# used to build a stage4
subarch: amd64
version_stamp: ceph-nomultilib-20150504
target: stage4
rel_type: container
profile: steveeJ:container/linux/amd64-native/ceph
snapshot: 20150504
source_subpath: ../download/stage3-amd64-nomultilib-20150430
portage_confdir: /var/tmp/catalyst/confdir
pkgcache_path: packages/container/amd64-nomultilib
portage_overlay: /usr/local/portage/personal-portage-overlay
stage4/packages: @profile
stage4/fsscript: container.fsscript
#stage4/root_overlay: ceph_root_overlay
stage4/empty: /var/tmp /var/cache

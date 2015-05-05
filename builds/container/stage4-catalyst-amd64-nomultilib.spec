# stage4 specfile
# used to build a stage4
subarch: amd64
version_stamp: stage4-catalyst-amd64-nomultilib-20150504
target: stage4
rel_type: container
profile: steveeJ:container/linux/amd64-native/catalyst
snapshot: 20150504
source_subpath: ../download/stage3-amd64-nomultilib-20150430
portage_confdir: /var/tmp/catalyst/confdir
pkgcache_path: packages/container/amd64-nomultilib
portage_overlay: /var/tmp/catalyst/overlay
stage4/packages: @profile
stage4/fsscript: /var/tmp/catalyst/builds/container.fsscript
#stage4/root_overlay: catalyst_root_overlay
stage4/empty: /var/tmp /var/cache

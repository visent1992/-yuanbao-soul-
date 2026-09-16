[app]
title = 元宝 Soul
package.name = yuansoul
package.domain = org.yuanbao

source.dir = .
source.include_exts = py,png,jpg,kv,json,db,ttf,atlas

version = 0.1

requirements = python3==3.11.9,kivy==2.3.0,cython==0.29.36,plyer,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.allow_backup = False
android.debug = True

p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 0

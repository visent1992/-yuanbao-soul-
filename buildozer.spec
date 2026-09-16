[app]
title = 元宝 Soul
package.name = yuansoul
package.domain = com.yuanbao
source.dir = .
source.include_exts = py,png,jpg,kv,json,db,ttf,atlas
version = 0.1
requirements = python3==3.11.9,kivy==2.3.0,plyer,requests,cython==0.29.36
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.allow_backup = False
android.debug = True

[buildozer]
log_level = 2
warn_on_root = 0

[app]
title = 元宝 Soul
package.name = yuansoul
package.domain = com.yuanbao
source.dir = .
source.include_exts = py,png,jpg,kv,json,db
version = 0.1
requirements = python3==3.11.0,kivy==2.3.0,plyer,requests,cython==0.29.36
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0

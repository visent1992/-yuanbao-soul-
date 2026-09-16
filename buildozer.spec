[app]
title = 元宝 Soul
package.name = yuansoul
package.domain = com.yuanbao
source.dir = .
source.include_exts = py,png,jpg,kv,json,db
version = 0.1

# 锁稳定版 Python 3.11，避开 3.14 配置死结
requirements = python3==3.11.9,kivy==2.3.0,plyer,requests,cython==0.29.36

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 0

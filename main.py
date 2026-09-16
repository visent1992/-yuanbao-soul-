[app]
title = yuanbao-soul
package.name = yuanbaosoul
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# 主类入口默认找 main.py 中的 App 类，若类名特殊需指定：
# source.main = main.py

requirements = python3==3.11.9,kivy==2.3.0,plyer,requests,cython==0.29.36
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

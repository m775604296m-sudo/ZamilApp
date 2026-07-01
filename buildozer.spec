[app]

# (string) Title of your application
title = زوامل إبراهيم الملصي

# (string) Package name
package.name = zamilapp

# (string) Package domain (needed for android packaging)
package.domain = org.alslbh

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,ttf,mp3

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*, assets/audio/*, assets/font/*, assets/images/*

# (string) Application version
version = 1.0

# (list) Application requirements
# قمنا بضبط الإصدارات بدقة هنا لضمان عمل الأيقونات والخطوط العربية بدون تعارض
requirements = python3,kivy==2.3.0,kivymd==1.1.1,arabic_reshaper,python-bidi,pillow

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions required by the app
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MODIFY_AUDIO_SETTINGS

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) If True, then skip trying to update the Android sdk automatically
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Icon of the application (تأكد من وجود هذه الصورة في مجلدك أو قم بتعديل المسار لأيقونة تطبيقك)
# android.icon.filename = %(source.dir)s/assets/images/avatar.png

# (str) Presplash of the application
# android.presplash.filename = %(source.dir)s/assets/images/avatar.png

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
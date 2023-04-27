Basic script for Bug Bounty program in order to:
1. Download apk from Google Play
2. Decompile apk
3. Search for common words like: firebase.io, username, password, apikey
4. Test connection to firebase.io/.json (if not "Access Denied")
5. Show results


# To do:
2. Checks SMALI config
3. build configs like - local.properties, gradle.properties
4. /data/misc/keystore/
5. https://github.com/dwisiswant0/apkleaks
6. Add print google api keys + urls
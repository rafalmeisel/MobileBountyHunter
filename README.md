# Mobile Bounty Hunter

## General
Mobile Bounty Hunter is an application that scan mobile application in order to find secrets/api keys/misconfigurations.

## Example of use

Mobile Bounty Hunter execute commands:

``` Python
# === Run the script (load applications from "storeUrls.txt") ===
python3 MobileBountyHunter.py -s

# === Help ===
python3 MobileBountyHunter.py -h

# === Scan specific application file ===
python3 MobileBountyHunter.py -f "com.google.android.googlequicksearchbox"

# === Input / Output directory ===
# To use input directory, you need to create it and paste mobile application there.
# Next, you need to specify Input (optionally output) directory
# By Default, inputDirectory and outputDirectory are located in workspace
python3 MobileBountyHunter.py -i /path/to/directory -o /path/to/output/directory

# === Download and analyze applications from the apksList.txt file (you need to specify application names in the file) ===
# Default apksListFile
python3 MobileBountyHunter.py -l
# Custom storeUrlsListFile
python3 MobileBountyHunter.py -apksListFile /path/to/apksListFile

# === Download and analyze applications from developer file ===
# Default storeUrlsListFile
python3 MobileBountyHunter.py -s
# Custom storeUrlsListFile
python3 MobileBountyHunter.py -storeUrlsListFile /path/to/storeUrlsListFile

# === Download and analyze application from specific url ===
python3 MobileBountyHunter.py -u 'https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox'
python3 MobileBountyHunter.py -url 'https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox'
```

### Examples of configuration files

``` Python
# === "storeUrls.txt" ===
https://play.google.com/store/apps/dev?id=5700313618786177705
https://play.google.com/store/apps/dev?id=6720847872553662727
https://play.google.com/store/apps/details?id=com.google.android.apps.walletnfcrel
https://play.google.com/store/apps/details?id=com.microsoft.office.officehubrow
https://apps.apple.com/pl/developer/google-llc/id281956209?l=pl
https://apps.apple.com/pl/app/google-one/id1451784328

# === apksListFile ===
com.google.android.googlequicksearchbox
com.android.chrome
com.google.android.apps.photos
```

## Example output

![](images/2023-05-03-07-20-16.png)

## Functionalities
This script was created to very quick find basic security issues in the application such as:

1. Android:
   - Android Manifest:
     - Exported activities   
   - Android Resource Values:
     - AWS keys
     - Google keys
     - Checking access to Firebase
     - Checking access to Google Maps APIs
   - Files:
    - Finding database files

2. iOS: 
   - Will be added in the future.


## Why this application was created?
On the market you can find great software to check mobile applications as:
- MobSF (https://github.com/MobSF/Mobile-Security-Framework-MobSF)
- ApkLeaks (https://github.com/dwisiswant0/apkleaks)

The only problem with these tools is that they are time-consuming. You need manually download the mobile application and run above tools against application. Mobile Bounty Hunter needs only link to Google Play / Apple Store (developer url, application url) and download all applications related to this URL automatically, decompiling and checking them.

The most important functionality and the idea of whole project is:
- to provide url to developer page of Store and automatically find and download all application that were published by this Developer,
- to check Firebase URL access and Google API Maps access.

Scans are based on checking mainly:
- Android: Manifest, resource Values
- iOS: will be added in the future


### Average time
Average time is 20-30 applications per hour.

### Example scenario
Let's assume that you are Bounty Hunter and you would like to search for security issues in mobile applications. You know that there are few companies to check:
- Company A - 20 applications in Google Play
- Company B - 30 applications in Google Play
- Company C - 10 applications in App Store

Now, you would like to find only basic issues (Low-hanging fruits as open Firebase or Google Api) to report them. Using Mobile Bounty Hunter, what you need to do is providing Companys URLs to Google Play/App Store. The Mobile Bounty Hunter automatically find all application that were published by these Companies, download them, decompile them, find the issues and report them to you (print in console and write the report).

Notice:
The Mobile Bounty Hunter is not full-penetration testing platform, it is rather "Low-hanging fruits" checker. If you want to scan whole application, please use MobSF (https://github.com/MobSF/Mobile-Security-Framework-MobSF).


## Disclaimer
The Mobile Bounty Hunter can be used ONLY for educational purpose and Bug Bounty activities to find the issues and report them to application developers. Any other activities (especially illegal) are forbidden.

## What kind of vulnerabilities are cheched, explanation how this knowledge could be used and if they are worth to report
1. Android:
   1. .db / .sql files:
      1. Why: Databases files can contain sensitive information about clients/configurations/tables.
      2. Next step: Read these files in order to find any sensitive informations.
      3. Worth to report: Depends.
   2. 



## Todo's:
1. Check build configs like: local.properties, gradle.properties
2. Check: /data/misc/keystore/
3. Prepare full scan including all files in decompiled application

## Interesting links about Mobile Bug Bounty:
https://www.youtube.com/watch?v=OlgmPxTHLuY
https://hackmd.io/@Chal13W1zz/ABBH
https://www.youtube.com/watch?v=S6xGOU-QWWQ

Checking WebViews
https://medium.com/mobis3c/exploiting-android-webview-vulnerabilities-e2bcff780892
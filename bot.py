import requests 
import random,datetime,sys 
from user_agent import generate_user_agent
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="_._._._._."
gd = str(generate_user_agent())

#-------------------------start code ---------------------------#
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/h
    jv
                        ',headers = {'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type': 'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':f'{gd}','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL','cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425','cookie':'ig_nrcb=1'},data=f'email=sgahahfdggsdfs%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(f"[:] ErRoR uSeR : {user}")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(f"[-] BaD uSeR : {user}")
    else:
        email=0
        print(f"[+] GooD uSeR :  {user}")
        email+=1
        god=f"""Done | @{user}"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="qwertyuiopasdfghjklzxcvbnm1234567890"
    while True:
         v1 = str(''.join((random.choice(insta) for i in range(1))))
         v2 = str(''.join((random.choice(insta) for i in range(1))))
         v3 = str(''.join((random.choice(insta) for i in range(1))))
         v4 = str(''.join((random.choice(insta) for i in range(1))))
         v5 = str(''.join((random.choice(all) for i in range(1))))
         user1 = (v2+v1+v1+v1+v2+v1)
         user2 = (v2+v1+v1+v2+v1+v1)
         user3 = (v2+v1+v2+v1+v1+v1)
         user4 = (v2+v1+v1+v1+v1+v2)
         user5 = (v1+v2+v1+v1+v1+v2)
         user6 = (v1+v2+v1+v1+v1+v1)
         user7 = (v1+v2+v1+v2+v1)
         user8 = (v1+v2+v2+v1+v1)
         user9 = (v1+v2+v2+v2+v1)
         user10 = (v2+v1+v1+v1+v2)
         user11 = (v1+v1+v2+'_'+v2)
         user12 = (v1+v1+v2+'_'+v1)
         user13 = (v1+v2+v2+'_'+v2)
         user14 = (v1+v2+v1+'_'+v2)
         user15 = (v2+v1+v2+'_'+v2)
         user16 = (v2+v1+v1+'_'+v2)
         user17 = (v1+v1+v2+'.'+v2)
         user18 = (v1+v1+v1+'.'+v2)
         user19 = (v2+v2+v2+'.'+v1)
         user20 = (v2+v2+v1+'.'+v1)
         user21 = (v1+v2+v1+'.'+v2)
         user22 = (v2+v1+v2+'.'+v1)
         user23 = (v1+v1+'.'+v1+v2)
         user24 = (v2+v1+'.'+v1+v1)
         user25 = (v1+'.'+v1+v1+v2)
         user26 = (v2+'.'+v2+v1+v1)
         user27 = (v2+'.'+v1+v2+v2)
         user28 = (v2+'.'+v1+v1+v2)
         user29 = (v1+'.'+v2+v2+v1)
         user30 = (v1+'.'+v1+v2+v2)
         user31 = (v1+'_'+v1+v2+v2)
         user32 = (v1+'_'+v2+v2+v2)
         user33 = (v2+'_'+v1+v2+v2)
         user34 = (v1+'_'+v1+v2+v1)
         user35 = (v2+'_'+v1+v2+v1)
         user36 = (v1+'_'+v2+v1+v2)
         user37 = (v1+'.'+v1+v2+v2)
         user38 = (v1+'.'+v1+v1+v2)
         user39 = (v1+'.'+v2+v2+v2)
         user40 = (v1+'.'+v2+v1+v2)
         user41 = (v2+'.'+v2+v1+v2)
         user42 = (v1+v1+'_'+v2+v2)
         user43 = ('_'+v1+v1+v2+v2)
         user44 = ('_'+v1+v2+v1+v2)
         user45 = ('_'+v2+v2+v1+v2)
         user46 = ('_'+v1+v2+v1+v1)
         user47 = ('_'+v1+v1+v1+v2)
         user48 = ('_'+v2+v2+v1+v1)
         user49 = (v1+'_'+'_'+v1+v2)
         user50 = (v2+'_'+'_'+v1+v1)
         user51 = (v2+v1+'_'+'_'+v1)
         user52 = (v1+v2+'_'+'_'+v2)
         user53 = (v1+'_'+v2+'_'+v1)
         user54 = (v2+'_'+v1+'_'+v2)
         user55 = (v1+'.'+v2+'.'+v1)
         user56 = (v2+'.'+v1+'.'+v2)
         user57 = ('_'+v1+'_'+v1+v2)
         user58 = ('.'+v1+'.'+v1+v2)
         user59 = ('_'+v1+'_'+v1+v1)
         user60 = ('_'+v2+'_'+v2+v1)
         user61 = ('_'+v2+'_'+v1+v1)
         user62 = ('_'+v2+'_'+v1+v2)
         user63 = ('_'+v1+'_'+v2+v1)
         user64 = ('_'+v2+'_'+v2+v2)
         user65 = ('_'+v1+'.'+v1+v2)
         user66 = ('_'+v1+'.'+v1+v1)
         user67 = ('_'+v2+'.'+v2+v1)
         user68 = ('_'+v2+'.'+v1+v1)
         user69 = ('_'+v1+'.'+v1+v2)
         user70 = ('_'+v2+'.'+v1+v2)
         user71 = ('_'+v1+'.'+v2+v1)
         user72 = ('_'+v2+'.'+v2+v2)
         abd = (user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15, user16, user17, user17, user18, user20, user21, user22, user23, user24, user25, user26, user27, user28, user29, user30, user31, user32, user33, user34, user35, user36, user37, user38, user39, user40, user41, user42, user43, user44, user45, user46, user47, user48, user49, user50, user51, user52, user53, user54, user55, user56, user57, user58, user59, user60, user61, user62, user63, user64, user65, user66, user67, user68, user69, user70, user71, user72)
         user = random.choice(abd)
         instaa(user)
id=input(f"EnTeR iD : ")
token=input(f"EnTeR ToKeN : ")
print()	
users()

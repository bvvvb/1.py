import requests,sys,os,json,random 
from rich import print as SS
from rich.panel import Panel as g
from rich.console import Console
from user_agent import generate_user_agent
Ss = Console()
ok,tok,bad=0,0,0
AB_KH='\033[37m'
AH_T='\033[91m'
AKH_T='\033[92m'
AS_F='\033[93m'
id = input('Enter iD : ')
token = input('Enter Token : ')
os.system('clear')
def us():
  saa="1234567890qwertyuiopasdfghjklzxcvbnm"
  while True:
         s = str(''.join((random.choice(saa) for i in range(1))))
         ss = str(''.join((random.choice(saa) for i in range(1))))
         sss = str(''.join((random.choice(saa) for i in range(1))))
         ee = str(''.join((random.choice(saa) for i in range(1))))
         e = str(''.join((random.choice(saa) for i in range(1))))
         u1 = (s+'_'+ee+'_'+sss)
         u2 = (sss+'_'+sss+'_'+ss)
         u3 = (s+'.'+ee+'.'+ss)
         u4 = (s+ss+'_'+ss+ss)
         u5 = (s+'_'+s+'_'+s)
         u6 = (s+'.'+s+'.'+s)
         u7 = (s+'_'+ee+'_'+ee)
         u8 = (s+'.'+ee+'.'+ee)
         u9 = ('_'+s+s+s+e)
         u10 = (ss+ee+ee+ee+ss)
         u11 = (ee+ee+sss+'_'+sss)
         u12 = (ee+ee+s+'_'+ee)
         u13 = (ee+e+e+'_'+e)
         u14 = (ss+ss+'.'+s+ss)
         j= (u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14)
         user = random.choice(j)
         sgg(user)
def sgg(user):
    gd = str(generate_user_agent())
    global ok,tok,bad
    sys.stdout.write(f'\r   {AKH_T}Done : {ok}{AB_KH} | BaD : {bad} {AB_KH} | TaKeN : {tok} {AKH_T}'),
    sys.stdout.flush()
    headers = {'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type': 'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':f'{gd}','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL','cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425','cookie':'ig_nrcb=1'
  }
    data= f'email=sgahahfdggsdfs%40gmail.com&username={user}&first_name=&opt_into_one_tap=false'
    res = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers=headers, data=data).text
#    res_dict = json.loads(res)
    if "status" in res and "fail" in res:
      bad+=1
    elif '"errors": {"username":' in res or '"code": "username_is_taken"' in res:
      tok+=1
    else:
      ok+=1
      print('\n')
      print('   '*10)
      gg = f'[green] \nuSer : {user} '
      SS(g(gg))
      tle = f"yo nigga iam abd : @{user}"
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={tle}')
#us()
import threading
for i in range(50):
 t=threading.Thread(target=us,args=())
 t.start()
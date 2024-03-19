import requests,os,random,threading
abc="qwertyuiopasdfghjklzxcvbnm1234567890"


ra=0
print(f"		[✓] Get username Available  <\>")
id = input(f'[✓] Enter ID : ')
token = input(f'[✓] Enter Token : ')
def checkuser():
    user1= str(''.join((random.choice(abc) for i in range(1))))
    user2= str(''.join((random.choice(abc) for i in range(1))))
    user3= str(''.join((random.choice(abc) for i in range(1))))
    user=(f"{user1}_{user2}{user3}__")
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
    	print(f"Username > {user} > [✘] Not Available ")
    	t = threading.Thread(target=checkuser)
    	t.start()
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
    	print(f"Username > {user} > [✘] Not Available ")
    	t = threading.Thread(target=checkuser)
    	t.start()
    else:
    	text=f'''
𓆩 𝒏𝒆𝒘 𝒖𝒔𝒆𝒓 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆  ! 
╭۪ᰲ╍ׂ╌ׂ╍۪ᰲ╮╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅׅ╍╌ᰲ╌ׅ╮
┊   𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆 : ❲@{user}❳
╰۫᷼╍ׅ╌ׅ╍۫᷼╯╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌᷼╌۫╯ ‌
𓆩 𝒃𝒚 : @kckkkkc !
'''
    	requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
    	print(f"Username > {user} > [✓] Available ")
    	t = threading.Thread(target=checkuser)
    	t.start()
#checkuser()
t = threading.Thread(target=checkuser)
t.start()

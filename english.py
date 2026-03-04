import requests
from bs4 import BeautifulSoup

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_daily_english():
    # 해커스 영어 매일 회화 페이지
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/daily_english"
    
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 오늘의 대화문 중 첫 번째 문장과 해석 가져오기
        # 사이트 구조에 따라 텍스트 위치를 찾습니다.
        en_text = soup.select_one('.conv_txt #daily_english_kor_msg_0').text.strip()
        ko_text = soup.select_one('.conv_txt #daily_english_kor_msg_0').find_next('p').text.strip()
        
        # 두 번째 문장도 가져오기 (총 2개)
        en_text2 = soup.select_one('.conv_txt #daily_english_kor_msg_1').text.strip()
        ko_text2 = soup.select_one('.conv_txt #daily_english_kor_msg_1').find_next('p').text.strip()

        return f"🇺🇸 오늘의 실생활 영어\n\n1️⃣ {en_text}\n(뜻: {ko_text})\n\n2️⃣ {en_text2}\n(뜻: {ko_text2})"
    
    except Exception as e:
        return "⚠️ 영어 문장을 가져오는 데 실패했습니다."

def send_telegram():
    content = get_daily_english()
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(send_url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_telegram()

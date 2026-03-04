import requests
from bs4 import BeautifulSoup

# 사용자님의 봇 정보
TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_daily_english():
    # 해커스 영어 매일 회화 페이지
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/daily_english"
    
    try:
        # 브라우저인 척 하기 위한 헤더 설정 (차단 방지)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 첫 번째 대화문 문장과 해석 가져오기
        en_text = soup.select_one('.conv_txt #daily_english_kor_msg_0').get_text().strip()
        ko_text = soup.select_one('.conv_txt #daily_english_kor_msg_0').find_next('p').get_text().strip()
        
        return f"🇺🇸 오늘의 실생활 영어\n\n✅ {en_text}\n(뜻: {ko_text})"
    
    except Exception as e:
        return f"⚠️ 영어 문장을 가져오는 데 실패했습니다: {str(e)}"

def send_telegram():
    content = get_daily_english()
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(send_url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_telegram()

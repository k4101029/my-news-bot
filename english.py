import requests
from bs4 import BeautifulSoup

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/daily_english"
    
    # 브라우저 정보(User-Agent)를 더 자세히 적어서 '진짜 사람'처럼 보이게 합니다.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status() # 접속 에러 시 예외 발생
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 문장 추출 (id가 정확한지 다시 한번 확인한 경로입니다)
        en_elem = soup.select_one('#daily_english_kor_msg_0')
        if en_elem:
            en = en_elem.get_text().strip()
            # 해석은 해당 문장 바로 다음의 <p> 태그에 있습니다.
            ko = en_elem.find_next('p').get_text().strip()
            return f"🇺🇸 오늘의 실생활 영어\n\n✅ {en}\n(뜻: {ko})"
        else:
            return "⚠️ 사이트 구조가 바뀌어 문장을 찾을 수 없습니다."
            
    except Exception as e:
        return f"⚠️ 접속 오류 발생: {str(e)}"

def send_msg():
    content = get_english()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

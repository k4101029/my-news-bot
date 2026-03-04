import requests
from bs4 import BeautifulSoup

# 사용자님의 봇 정보
TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_naver_english():
    # 네이버 오늘의 영어회화 주소
    url = "https://learn.dict.naver.com/conversation#/enko/today"
    
    try:
        # 네이버는 동적 페이지라 모바일 웹 버전으로 접근하는 게 문장을 가져오기 쉽습니다.
        mobile_url = "https://m.wordbook.naver.com/endic/today/conversation.nhn"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
        }
        
        res = requests.get(mobile_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 첫 번째 대화 문장 추출
        en_part = soup.select_one('.txt_english')
        ko_part = soup.select_one('.txt_origin')
        
        if en_part and ko_part:
            en_text = en_part.get_text().strip()
            ko_text = ko_part.get_text().strip()
            return f"🇰🇷 네이버 오늘의 영어\n\n✅ {en_text}\n(뜻: {ko_text})"
        else:
            # 구조가 다를 경우 대비한 예비 추출 방식
            sentences = soup.select('.item_con')
            if sentences:
                en = sentences[0].select_one('.txt_en').get_text().strip()
                ko = sentences[0].select_one('.txt_ko').get_text().strip()
                return f"🇰🇷 네이버 오늘의 영어\n\n✅ {en}\n(뜻: {ko})"
            
            return "⚠️ 문장을 찾는 데 실패했습니다. (네이버 구조 변경 가능성)"
            
    except Exception as e:
        return f"⚠️ 접속 오류 발생: {str(e)}"

def send_msg():
    content = get_naver_english()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

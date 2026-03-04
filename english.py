import requests
from bs4 import BeautifulSoup

# 사용자님의 봇 정보
TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_english_phrase():
    # 주소 에러가 적은 대체 사이트 (YBM 오늘의 회화)
    url = "https://www.ybmedu.com/2018/com_daily_conversation.asp"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=15)
        res.encoding = 'utf-8' # 한글 깨짐 방지
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # YBM 사이트에서 영어 문장과 한글 해석 찾기
        en_part = soup.select_one('.daily_conv_top .en')
        ko_part = soup.select_one('.daily_conv_top .ko')
        
        if en_part and ko_part:
            en_text = en_part.get_text().strip()
            ko_text = ko_part.get_text().strip()
            return f"📚 오늘의 추천 영어 회화\n\n✅ {en_text}\n(뜻: {ko_text})"
        else:
            return "⚠️ 문장 위치를 찾을 수 없습니다. (사이트 구조 변경)"
            
    except Exception as e:
        return f"⚠️ 접속 오류 발생: {str(e)}"

def send_msg():
    content = get_english_phrase()
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(send_url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

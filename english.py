import requests
from bs4 import BeautifulSoup

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_google_english():
    # 구글 뉴스에서 'Learning English' 검색 결과 (RSS 피드 방식 - 차단 없음)
    url = "https://news.google.com/rss/search?q=Learning+English+phrase&hl=en-US&gl=US&ceid=US:en"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.content, 'xml') # RSS는 xml 형식을 사용합니다.
        
        # 최신 뉴스 아이템 3개 가져오기
        items = soup.find_all('item')[:3]
        
        if not items:
            return "⚠️ 구글 뉴스에서 정보를 찾을 수 없습니다."
            
        result_text = "🌐 Google News: 오늘의 영어 학습\n\n"
        
        for i, item in enumerate(items, 1):
            title = item.title.text
            link = item.link.text
            result_text += f"{i}. {title}\n🔗 {link}\n\n"
            
        return result_text
            
    except Exception as e:
        return f"⚠️ 구글 접속 실패: {str(e)}"

def send_msg():
    content = get_google_english()
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(send_url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

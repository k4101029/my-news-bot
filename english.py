import requests
from bs4 import BeautifulSoup

# 사용자님의 봇 정보
TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_donga_english():
    # 동아일보 오늘의 영어회화 주소
    url = "https://www.donga.com/news/List/Column/TodayEnglish"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        # 1. 목록 페이지에서 가장 최신 글의 링크를 찾습니다.
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 첫 번째 기사 링크 추출
        latest_post = soup.select_one('.articleList .tit a')
        if not latest_post:
            return "⚠️ 최신 글 링크를 찾을 수 없습니다."
            
        post_url = latest_post['href']
        
        # 2. 해당 글 안으로 들어가서 영어 문장을 가져옵니다.
        res_post = requests.get(post_url, headers=headers, timeout=10)
        soup_post = BeautifulSoup(res_post.text, 'html.parser')
        
        # 본문 내용 추출 (동아일보는 보통 본문 상단에 영어/한글이 같이 나옵니다)
        content = soup_post.select_one('.article_txt').get_text()
        
        # 본문에서 필요한 부분만 예쁘게 자르기 (보통 A: 영어 / B: 영어 형태)
        # 너무 길면 텔레그램으로 보기 힘드니 앞부분 5줄 정도만 가져옵니다.
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        display_text = "\n".join(lines[:6]) # 상단 대화문 위주로 추출
        
        return f"📰 동아일보 오늘의 회화\n\n{display_text}"
            
    except Exception as e:
        return f"⚠️ 자동 추출 실패: {str(e)}"

def send_msg():
    content = get_donga_english()
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(send_url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

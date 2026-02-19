import requests
from bs4 import BeautifulSoup
import urllib.parse

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'
KEYWORD = '비트코인'

def run_now():
    encoded_keyword = urllib.parse.quote(KEYWORD)
    url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ko&gl=KR&ceid=KR:ko"
    
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.content, 'xml')
        items = soup.find_all('item')
        
        if items:
            msg_content = [f"🤖 [자동발송] 오늘의 {KEYWORD} 뉴스\n"]
            for item in items[:5]:
                msg_content.append(f"📌 {item.title.text}\n🔗 {item.link.text}")
            
            final_msg = "\n\n".join(msg_content)
            send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            requests.post(send_url, data={'chat_id': CHAT_ID, 'text': final_msg})
            print("Successfully sent to Telegram")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_now()

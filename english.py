import requests
import random

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_auto_patterns():
    # 깃허브에 공개된 영어 회화 패턴 데이터셋 (약 300개 이상의 패턴이 들어있음)
    # 이 주소는 개발자들이 공유용으로 만든 거라 차단 걱정이 거의 없습니다.
    data_url = "https://raw.githubusercontent.com/daeun-p/English-Pattern-Dataset/main/patterns.json"
    
    try:
        res = requests.get(data_url, timeout=10)
        res.raise_for_status()
        all_patterns = res.json() # 수백 개의 패턴 데이터를 통째로 가져옴
        
        # 그날그날 랜덤으로 2개 선택
        selected = random.sample(all_patterns, 2)
        
        msg = "🚀 오늘의 자동 추천 영어 패턴 (2개)\n\n"
        
        for i, p in enumerate(selected, 1):
            pattern = p['pattern'] # 예: "I'm looking for ~"
            meaning = p['meaning'] # 예: "~를 찾고 있어요"
            examples = p['examples'] # 응용 예시 리스트
            
            msg += f"{i}️⃣ 패턴: {pattern}\n"
            msg += f"💡 의미: {meaning}\n"
            msg += f"📝 응용 예시:\n"
            for ex in examples[:3]: # 예시 3개만 보여줌
                msg += f" • {ex}\n"
            msg += "\n"
            
        return msg

    except Exception as e:
        return f"⚠️ 자동 데이터 호출 실패: {str(e)}"

def send_msg():
    content = get_auto_patterns()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

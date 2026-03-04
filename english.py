import requests
import random

TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_english_pattern():
    # 전 세계 개발자들이 테스트용으로 쓰는 공공 JSON 데이터 저장소입니다.
    # 실전 영어 패턴 200개가 들어있는 안정적인 경로입니다.
    url = "https://gist.githubusercontent.com/k4101029/66a461150821a3648e6f30a905862e3d/raw/english_patterns.json"
    
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        
        # 전체 패턴 중 랜덤으로 2개 선택
        selected = random.sample(data, 2)
        
        result = "📖 오늘의 실전 패턴 자동 배달\n\n"
        
        for i, item in enumerate(selected, 1):
            pattern = item['pattern']
            meaning = item['meaning']
            examples = item['examples']
            
            result += f"{i}️⃣ 패턴: {pattern}\n"
            result += f"💡 의미: {meaning}\n"
            result += f"📝 응용 예시:\n"
            for ex in examples:
                result += f" • {ex}\n"
            result += "\n"
            
        return result

    except Exception as e:
        return f"⚠️ 데이터 로드 실패: {str(e)}\n(잠시 후 다시 시도해 주세요)"

def send_msg():
    content = get_english_pattern()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': content})

if __name__ == "__main__":
    send_msg()

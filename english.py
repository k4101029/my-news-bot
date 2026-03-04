import requests
import random

# 사용자님의 봇 정보
TOKEN = '8360600183:AAEL_ZH_cCEwz7uxCpiiUoPqbFBXrys2T4I'
CHAT_ID = '6280490264'

def get_pattern_study():
    # 📚 [실전 영어 패턴 60 데이터베이스]
    data = [
        {"p": "I'm looking for ~", "m": "~를 찾고 있어요", "e": ["a gift for my mom.", "the nearest station.", "a job here."]},
        {"p": "Could you help me with ~?", "m": "~하는 것 좀 도와주실래요?", "e": ["this heavy bag.", "my homework.", "finding the exit."]},
        {"p": "I'm planning to ~", "m": "~할 계획이에요", "e": ["travel abroad.", "start a new hobby.", "buy a new car."]},
        {"p": "Do you mind if I ~?", "m": "제가 ~해도 괜찮을까요?", "e": ["sit here?", "open the window?", "ask a question?"]},
        {"p": "I'm used to ~ing", "m": "~하는 것에 익숙해요", "e": ["waking up early.", "driving in the city.", "working late."]},
        {"p": "It's time to ~", "m": "~할 시간이에요", "e": ["go to bed.", "make a decision.", "take a break."]},
        {"p": "I'm about to ~", "m": "막 ~하려는 참이에요", "e": ["leave the house.", "have dinner.", "call you back."]},
        {"p": "I have no idea ~", "m": "~를 전혀 모르겠어요", "e": ["how to use this.", "what he said.", "where they are."]},
        {"p": "How about ~ing?", "m": "~하는 건 어때요?", "e": ["ordering pizza?", "going for a walk?", "watching a movie?"]},
        {"p": "I'd like to ~", "m": "~하고 싶어요", "e": ["book a table.", "check out now.", "try this on."]},
        {"p": "I'm interested in ~", "m": "~에 관심이 있어요", "e": ["learning English.", "your project.", "buying a house."]},
        {"p": "It takes (time) to ~", "m": "~하는 데 (시간이) 걸려요", "e": ["10 minutes to walk.", "an hour to get there.", "years to master."]},
        {"p": "Don't forget to ~", "m": "~하는 거 잊지 마세요", "e": ["lock the door.", "bring your umbrella.", "call me later."]},
        {"p": "I'm sorry for ~ing", "m": "~해서 죄송합니다", "e": ["being late.", "keeping you waiting.", "making a mistake."]},
        {"p": "You'd better ~", "m": "~하는 게 좋을 거예요", "e": ["see a doctor.", "hurry up.", "stay home today."]},
        {"p": "I'm not sure if ~", "m": "~인지 잘 모르겠어요", "e": ["I can go.", "it's true.", "he will come."]},
        {"p": "Thank you for ~ing", "m": "~해주셔서 감사합니다", "e": ["inviting me.", "helping me out.", "listening to me."]},
        {"p": "I can't wait to ~", "m": "~하는 게 너무 기대돼요", "e": ["see you again.", "go on vacation.", "start the show."]},
        {"p": "It's no use ~ing", "m": "~해도 소용없어요", "e": ["crying over it.", "complaining now.", "trying to hide it."]},
        {"p": "Have you ever ~ed?", "m": "~해본 적 있나요?", "e": ["been to Paris?", "eaten sushi?", "met a famous person?"]},
        {"p": "I'm thinking of ~ing", "m": "~할까 생각 중이에요", "e": ["buying a bike.", "moving to Seoul.", "taking a yoga class."]},
        {"p": "Feel free to ~", "m": "마음 놓고 ~하세요", "e": ["ask questions.", "use my phone.", "come by anytime."]},
        {"p": "I was wondering if ~", "m": "~인지 궁금해요 (조심스러운 부탁)", "e": ["you could help me.", "we could meet today.", "this is available."]},
        {"p": "All you have to do is ~", "m": "당신은 ~하기만 하면 돼요", "e": ["press this button.", "sign your name.", "wait for a minute."]},
        {"p": "It's worth ~ing", "m": "~할 가치가 있어요", "e": ["watching this movie.", "visiting the museum.", "reading the book."]},
        {"p": "I'm supposed to ~", "m": "~하기로 되어 있어요", "e": ["meet him at 5.", "finish this today.", "be there early."]},
        {"p": "No matter how ~", "m": "아무리 ~해도", "e": ["hard I try.", "busy you are.", "expensive it is."]},
        {"p": "I'm afraid (that) ~", "m": "유감스럽게도 ~인 것 같아요", "e": ["I can't help you.", "we are late.", "it's sold out."]},
        {"p": "How long does it take to ~?", "m": "~하는 데 얼마나 걸리나요?", "e": ["get to the airport?", "finish the project?", "fix this laptop?"]},
        {"p": "I'm looking forward to ~ing", "m": "~하기를 고대하고 있어요", "e": ["hearing from you.", "meeting your family.", "starting the job."]},
        {"p": "Make sure to ~", "m": "반드시 ~하도록 하세요", "e": ["save the file.", "turn off the lights.", "wear a mask."]},
        {"p": "I happened to ~", "m": "우연히 ~하게 됐어요", "e": ["see him there.", "find the old photo.", "hear the news."]},
        {"p": "I'm worried about ~", "m": "~가 걱정돼요", "e": ["the interview.", "my health.", "the weather."]},
        {"p": "I don't feel like ~ing", "m": "~하고 싶지 않아요 (기분이 아님)", "e": ["going out.", "studying tonight.", "eating anything."]},
        {"p": "That's why ~", "m": "그게 바로 ~한 이유예요", "e": ["I'm late.", "I like you.", "I called you."]},
        {"p": "Is it okay if I ~?", "m": "제가 ~해도 될까요?", "e": ["use your pen?", "park here?", "leave early?"]},
        {"p": "I'm calling to ~", "m": "~하려고 전화드렸어요", "e": ["make a reservation.", "ask for help.", "say thank you."]},
        {"p": "You should try ~ing", "m": "~해보는 게 어때요? (권유)", "e": ["drinking green tea.", "using this app.", "talking to her."]},
        {"p": "I have to ~", "m": "~해야만 해요", "e": ["go now.", "finish my work.", "clean my room."]},
        {"p": "It's hard to ~", "m": "~하기가 힘들어요", "e": ["understand this.", "wake up early.", "say goodbye."]},
        {"p": "May I ~?", "m": "제가 ~해도 될까요? (정중)", "e": ["see your ID?", "take your order?", "help you?"]},
        {"p": "I want you to ~", "m": "당신이 ~해주면 좋겠어요", "e": ["stay here.", "tell me the truth.", "come with me."]},
        {"p": "I'm ready to ~", "m": "~할 준비가 됐어요", "e": ["order now.", "start the lesson.", "go out."]},
        {"p": "Wait until ~", "m": "~할 때까지 기다리세요", "e": ["I come back.", "the light turns green.", "further notice."]},
        {"p": "I can't afford to ~", "m": "~할 형편이 안 돼요", "e": ["buy a new car.", "waste time.", "lose this job."]},
        
        # ✨ 새로 추가된 15개 패턴 (총 60개) ✨
        {"p": "I'll let you know ~", "m": "~를 알려 드릴게요", "e": ["the results soon.", "when I'm ready.", "if I find it."]},
        {"p": "I'm calling about ~", "m": "~에 관해 전화 드렸어요", "e": ["the job opening.", "your lost bag.", "the reservation."]},
        {"p": "I'm on my way to ~", "m": "~로 가는 중이에요", "e": ["pick you up.", "the office.", "your house now."]},
        {"p": "You don't have to ~", "m": "~하지 않아도 돼요", "e": ["hurry up.", "bring anything.", "pay for this."]},
        {"p": "I'm not good at ~ing", "m": "~를 잘 못해요", "e": ["cooking pasta.", "singing in public.", "speaking English."]},
        {"p": "The point is ~", "m": "요점은 ~예요", "e": ["we need more time.", "it's too expensive.", "he doesn't know."]},
        {"p": "I'm busy ~ing", "m": "~하느라 바빠요", "e": ["doing my laundry.", "writing a report.", "preparing for lunch."]},
        {"p": "It's easy to ~", "m": "~하기 쉬워요", "e": ["forget people's names.", "get lost here.", "make mistakes."]},
        {"p": "I'd rather ~", "m": "차라리 ~하고 싶어요", "e": ["stay home.", "eat pizza.", "walk than drive."]},
        {"p": "What if ~?", "m": "만약 ~하면 어쩌죠?", "e": ["it rains tomorrow?", "I miss the bus?", "he says no?"]},
        {"p": "There is no need to ~", "m": "~할 필요 없어요", "e": ["worry about it.", "explain again.", "buy a new one."]},
        {"p": "I'm glad to ~", "m": "~하게 되어 기뻐요", "e": ["hear the news.", "see you again.", "meet your family."]},
        {"p": "As far as I know, ~", "m": "제가 알기로는 ~예요", "e": ["he is away.", "it's already closed.", "she is married."]},
        {"p": "I promise to ~", "m": "~하기로 약속할게요", "e": ["be there on time.", "call you tonight.", "keep it a secret."]},
        {"p": "I'm in the middle of ~ing", "m": "한창 ~하는 중이에요", "e": ["having lunch.", "cleaning the house.", "watching a movie."]}
    ]

    # 2개 패턴 무작위 선택
    selected = random.sample(data, 2)
    
    result = "🌟 [자동 배달] 오늘의 실전 영어 패턴\n\n"
    
    for i, item in enumerate(selected, 1):
        p, m, es = item['p'], item['m'], item['e']
        result += f"{i}️⃣ 패턴: {p}\n"
        result += f"💡 의미: {m}\n"
        result += f"📝 응용 예시:\n"
        for ex in es:
            # '~' 부분을 예시 문장으로 치환
            if '~ing' in p:
                sentence = p.replace('~ing', ex)
            else:
                sentence = p.replace('~', ex)
            result += f" • {sentence}\n"
        result += "\n"
        
    return result

def send_msg():
    content = get_pattern_study()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        res = requests.post(url, data={'chat_id': CHAT_ID, 'text': content})
        res.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_msg()

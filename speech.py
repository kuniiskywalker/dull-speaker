import speech_recognition as sr
import jtalk
import random

from get_bot_message import get_bot_message

def run():
    
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        jtalk.run('認識を開始します')
        recognizing = True
        while recognizing:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
    
                recognized_text = r.recognize_google(audio, language='ja-JP')
    
                print(recognized_text)
    
                bot_message = get_bot_message(recognized_text)
    
                print(bot_message)
    
                jtalk.run(bot_message)
            except KeyboardInterrupt:
                recognizing = False
                jtalk.run('認識を終了します')
                print('finish')
            except:
    
                messages = [
                    'ほげー',
                    'もんげー',
                ]
    
                # jtalk.run(random.choice(messages))
                print('故意にエラーを発生')

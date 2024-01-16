
import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Say something please !")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)  # 还可以选择不同的数据源，从而用来识别不同的语言
            print("You said : {}".format(text))

        except:
            print("Sorry I can't hear you!")
'''
import speech_recognition as sr
import logging

logging.basicConfig(level=logging.DEBUG)

while True:
    r = sr.Recognizer()
    # Mic
    mic = sr.Microphone()
    logging.info('message enter')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    logging.info('message end and recognize')
    test = r.recognize_google(audio, language='cmn-Hans-CN', show_all=True)
    print(test)
    logging.info('end')
'''
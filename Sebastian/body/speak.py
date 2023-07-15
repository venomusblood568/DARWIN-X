# link of the article i followed
#https://www.codesempai.com/2023/01/add-300-natural-voices-in-your.html

import os
import pygame
# cool voice i found
#en-US-EricNeural = male
#es-US-AlonsoNeural = male 
#en-US-AriaNeural =female
#en-US-AnaNeural = kid female
#en-US-ChristopherNeural = perfect male voice
# en-US-GuyNeural = this is also good
def speak(data):
    voice = 'en-US-AriaNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

speak("hello sir my name is aisha and i am at your service")
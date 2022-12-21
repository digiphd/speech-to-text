import whisper
import re

class Speech2Text:

    def __init__(self):
        pass

    def wrap_by_word(self, s, n):
        '''returns a string where \\n is inserted between every n words'''
        a = s.split()
        ret = ''
        for i in range(0, len(a), n):
            ret += ' '.join(a[i:i + n]) + '\n'

        return ret

    def transcribe_audio(self, audio):
        model = whisper.load_model("tiny")
        # model = whisper.load_model("base")
        # model = whisper.load_model("small") # Takes too Long for long audio greater than 5mins.
        result = model.transcribe(audio,  fp16=False, language='English')

        text = result['text']

        # Format text to have rough paragraphs and new lines.
        text = self.wrap_by_word(text, 15)
        pat = ('(?<!Dr)(?<!Esq)\.')
        text = re.sub(pat,'.\n\n',text)

        with open("../Output.txt", "w") as text_file:
            text_file.write(text)
        return result["text"]



if __name__ == "__main__":
    audio_file = '/Users/roger/Downloads/part 4 how to choose a ute.mp4'
    Whisper = Speech2Text()
    print(Whisper.transcribe_audio(audio_file))
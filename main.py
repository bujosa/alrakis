from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
    WOMAN: Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
    MAN: It is a pleasure to meet you, Suno. I also enjoy pizza and tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)

write_wav("./audio/audio.wav", SAMPLE_RATE, audio_array)
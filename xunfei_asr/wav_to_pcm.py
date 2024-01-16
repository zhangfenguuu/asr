import wave
def wav_to_pcm(input_file, output_file):
    with wave.open(input_file, 'rb') as wav_file:
        with open(output_file, 'wb') as pcm_file:
            pcm_file.write(wav_file.readframes(wav_file.getnframes()))

#wav_to_pcm('jj.wav','jj.pcm')
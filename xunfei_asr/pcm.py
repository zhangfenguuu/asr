import pyaudio
import wave
import numpy as np
import ffmpeg
def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    pcm_file=open(pcmfile, "wb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=data_type)
    data.tofile(pcm_file)
    f.close()
    pcm_file.close()

import wave

def wav_to_pcm(input_file, output_file):
    with wave.open(input_file, 'rb') as wav_file:
        with open(output_file, 'wb') as pcm_file:
            pcm_file.write(wav_file.readframes(wav_file.getnframes()))


def output_pcm(wavfile, pcmfile):
# 设置参数
    CHUNK = 1280  # 每次读取的音频数据大小
    FORMAT = pyaudio.paInt16  # 采样位数
    CHANNELS = 1  # 声道数
    RATE = 44100  # 采样率
    RECORD_SECONDS = 5  # 录音时长
    WAVE_OUTPUT_FILENAME = wavfile  # 输出文件名

    # 初始化PyAudio
    audio = pyaudio.PyAudio()

    # 打开麦克风进行录音
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("开始录音...")

    frames = []

    # 录音并将音频数据存储到frames列表中
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束.")

    # 停止录音并关闭流
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 将音频数据写入到WAV文件中
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print("音频已保存为PCM格式的WAV文件：", WAVE_OUTPUT_FILENAME)

    wav2pcm(wavfile, pcmfile)
    wav_to_pcm(wavfile, 'bb.pcm')
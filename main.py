import sounddevice as sd
from scipy.io.wavfile import write

# sample rate
fs = 44100

# Ask to enter a record time
second = int(input("Enter the Recording Time in seconds: "))

print("Recording...\n")
record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2)
sd.wait()
write('output.wav', fs, record_voice)
print("My Recording is done. Please check your folder to listen to the recording.")

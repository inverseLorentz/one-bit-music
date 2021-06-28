# one-bit-music
Program to create one-bit music from text files (may sound strange on some speakers/headphones). Does not support duty cycles other than 50% yet.

## Use
Run the python file `onebit.py` and then run
```python
compile_text('/path/to/inputfile.txt', '/path/to/outputfile.pcm')
```

## Specifications
Input is a text file, output is a raw mono unsigned 8-bit PCM file with a 44100 Hz sample rate. You can convert this into a WAV file using the FFmpeg command `ffmpeg -f u8 -ar 44100 -ac 1 -i input.file output.wav` or open it in Audacity by importing raw data and selecting "Unsigned 8-bit PCM" and "1 Channel (Mono)".

## Input format
The input consists of lines of four space-separated numbers. Each line is called an event.

The first number in an event dictates the type of sound. 0 means noise and 1 means a pulse wave.
The second number dictates the lowness of the noise (minimum 1 for highest noise) or the MIDI note number of the pulse wave.
The third number dictates if the event is a audible (1) or silent (0)
The fourth number dictates the length of the event in samples.

I have created a simple VAD program in Python for live time VAD through microphone. It is very lightweight. Feel free to use it!

It detecs voice activity using WebRTC, obtained from [py-webrtcvad](https://github.com/wiseman/py-webrtcvad)

To record the mic, the [sounddevice](https://python-sounddevice.readthedocs.io/en/0.5.1/) module is used

The requirements for running the file are installing those two module + numpy:
```
pip install sounddevice webrtcvad numpy
```

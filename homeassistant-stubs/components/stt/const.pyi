from _typeshed import Incomplete
from enum import Enum

DOMAIN: str
DATA_PROVIDERS: Incomplete

class AudioCodecs(str, Enum):
    PCM: str
    OPUS: str

class AudioFormats(str, Enum):
    WAV: str
    OGG: str

class AudioBitRates(int, Enum):
    BITRATE_8: int
    BITRATE_16: int
    BITRATE_24: int
    BITRATE_32: int

class AudioSampleRates(int, Enum):
    SAMPLERATE_8000: int
    SAMPLERATE_11000: int
    SAMPLERATE_16000: int
    SAMPLERATE_18900: int
    SAMPLERATE_22000: int
    SAMPLERATE_32000: int
    SAMPLERATE_37800: int
    SAMPLERATE_44100: int
    SAMPLERATE_48000: int

class AudioChannels(int, Enum):
    CHANNEL_MONO: int
    CHANNEL_STEREO: int

class SpeechResultState(str, Enum):
    SUCCESS: str
    ERROR: str

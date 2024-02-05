from .const import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, SpeechResultState as SpeechResultState
from dataclasses import dataclass

@dataclass
class SpeechMetadata:
    language: str
    format: AudioFormats
    codec: AudioCodecs
    bit_rate: AudioBitRates
    sample_rate: AudioSampleRates
    channel: AudioChannels
    def __post_init__(self) -> None: ...
    def __init__(self, language, format, codec, bit_rate, sample_rate, channel) -> None: ...

@dataclass
class SpeechResult:
    text: str | None
    result: SpeechResultState
    def __init__(self, text, result) -> None: ...

from .const import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, SpeechResultState as SpeechResultState
from _typeshed import Incomplete
from dataclasses import dataclass

@dataclass
class SpeechMetadata:
    language: str
    format: AudioFormats
    codec: AudioCodecs
    bit_rate: AudioBitRates
    sample_rate: AudioSampleRates
    channel: AudioChannels

@dataclass
class SpeechResult:
    text: str | None
    result: SpeechResultState

@dataclass
class SpeechAudioProcessing:
    requires_external_vad: bool
    prefers_auto_gain_enabled: bool
    prefers_noise_reduction_enabled: bool

DEFAULT_AUDIO_PROCESSING: Incomplete

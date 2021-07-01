import av
from . import redact_credentials as redact_credentials
from .const import AUDIO_CODECS as AUDIO_CODECS, MAX_MISSING_DTS as MAX_MISSING_DTS, MAX_TIMESTAMP_GAP as MAX_TIMESTAMP_GAP, MIN_SEGMENT_DURATION as MIN_SEGMENT_DURATION, PACKETS_TO_WAIT_FOR_AUDIO as PACKETS_TO_WAIT_FOR_AUDIO, SEGMENT_CONTAINER_FORMAT as SEGMENT_CONTAINER_FORMAT, SOURCE_TIMEOUT as SOURCE_TIMEOUT, TARGET_PART_DURATION as TARGET_PART_DURATION
from .core import Part as Part, Segment as Segment, StreamOutput as StreamOutput
from collections.abc import Mapping
from io import BytesIO
from threading import Event
from typing import Any, Callable

_LOGGER: Any

class SegmentBuffer:
    _stream_id: int
    _outputs_callback: Any
    _sequence: int
    _segment_start_dts: Any
    _memory_file: Any
    _av_output: Any
    _input_video_stream: Any
    _input_audio_stream: Any
    _output_video_stream: Any
    _output_audio_stream: Any
    _segment: Any
    _memory_file_pos: Any
    _part_start_dts: Any
    _part_has_keyframe: bool
    def __init__(self, outputs_callback: Callable[[], Mapping[str, StreamOutput]]) -> None: ...
    @staticmethod
    def make_new_av(memory_file: BytesIO, sequence: int, input_vstream: av.video.VideoStream) -> av.container.OutputContainer: ...
    def set_streams(self, video_stream: av.video.VideoStream, audio_stream: Any) -> None: ...
    def reset(self, video_dts: int) -> None: ...
    def mux_packet(self, packet: av.Packet) -> None: ...
    def check_flush_part(self, packet: av.Packet) -> None: ...
    def flush(self, packet: av.Packet, last_part: bool) -> None: ...
    def discontinuity(self) -> None: ...
    def close(self) -> None: ...

def stream_worker(source: str, options: dict[str, str], segment_buffer: SegmentBuffer, quit_event: Event) -> None: ...

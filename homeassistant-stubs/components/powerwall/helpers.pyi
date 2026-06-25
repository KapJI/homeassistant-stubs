from tesla_powerwall import ApiError as ApiError

_API_404_MARKER: str

def is_api_404(err: ApiError) -> bool: ...

from dataclasses import dataclass
from python_overseerr import IssueCount as IssueCount, RequestCount as RequestCount

@dataclass
class OverseerrData:
    requests: RequestCount
    issues: IssueCount

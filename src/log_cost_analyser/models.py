import dataclasses

@dataclasses.dataclass
class Finding:
    """A finding from an analyser."""
    analyser: str
    severity: str
    message: str
    data: dict

@dataclasses.dataclass
class AnalysisReport:
    """The result of running the analysers against a log set."""
    total_lines: int
    total_bytes: int
    findings: list[Finding]
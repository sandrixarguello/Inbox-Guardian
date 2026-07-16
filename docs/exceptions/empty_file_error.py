from .inbox_guardian_error import InboxGuardianError


class EmptyFileError(InboxGuardianError):
    """El archivo HTML está vacío."""
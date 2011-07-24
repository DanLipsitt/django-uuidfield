import base64
import uuid


def to_short_string(value):
    return base64.urlsafe_b64encode(value.bytes).rstrip('=')


def from_short_string(value, ignore_errors=False):
    try:
        return uuid.UUID(bytes=base64.urlsafe_b64decode(
            '{value}{padding}'.format(
                value=value,
                padding=len(value) % 4 * '='
            )
        ))
    except (TypeError, ValueError):
        if not ignore_errors:
            raise

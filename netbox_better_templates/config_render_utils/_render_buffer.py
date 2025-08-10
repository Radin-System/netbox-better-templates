from typing import Dict, List, Mapping, Optional, cast
#from django.conf import settings
from .._type_alisaes import MESSAGE_LEVELS

DEBUG: bool = True

messages: Mapping[str, Dict[str, str]] = {
    "debug": {
        "level": "debug",
        "message": "{msg}",
        "fix": "{fix}",
    },
    "info": {
        "level": "info",
        "message": "{msg}",
        "fix": "{fix}",
    },
    "warning": {
        "level": "warning",
        "message": "{msg}",
        "fix": "{fix}",
    },
    "error": {
        "level": "error",
        "message": "{msg}",
        "fix": "{fix}",
    },
    "default_value": {
        "level": "warning",
        "message": "Default value is used for `{name}`",
        "fix": "Provide a value for `{name}`",
    },
    "custom_field_missing": {
        "level": "error",
        "message": "Custom field `{name}` is missing",
        "fix": "create custum field for `{name}`, read docs for guidence.",
    },
    "context_missing": {
        "level": "error",
        "message": "Context `{name}` is missing",
        "fix": "create context for `{name}`, read docs for guidence.",
    },
    "invalid_context": {
        "level": "error",
        "message": "Invalid context `{name}`",
        "fix": "create valid context for `{name}`, read docs for guidence.",
    },
    "value_missing": {
        "level": "error",
        "message": "Value for `{name}` is missing",
        "fix": "Provide a value for `{name}` field or relation",
    },
    "invalid_value": {
        "level": "error",
        "message": "Invalid value `{value}` for `{name}`",
        "fix": "Provide a valid value for `{name}`",
    },
    "not_implemented": {
        "level": "debug",
        "message": "`{name}` Not implemented",
        "fix": "Contact developers.",
    },
    "not_enabled": {
        "level": "warning",
        "message": "This feature or context is not enabled `{name}`.",
        "fix": "Enable `{name}`",
    },
    "not_secure": {
        "level": "warning",
        "message": "Using this method or protocol is not secure `{name}`",
        "fix": "Use an alternative secure method or protocol.",
    },
}

class _RenderMessage:
    def __init__(
            self,
            buffer: "RenderBuffer",
            message_key: str,
            level: Optional[MESSAGE_LEVELS],
            **kwargs: str
        ) -> None:
        self._buffer = buffer
        self._message_key = message_key
        self._kwargs = kwargs

        message = messages.get(self._message_key)
        self._text = message.get("message", "Undefined") if message else "Undefined"
        self._fix = message.get("fix", "Undefined") if message else "Undefined"

        _level = level or (message.get("level", "info") if message else "info")
        self._level: MESSAGE_LEVELS = cast(MESSAGE_LEVELS, _level)

    def render(self) -> str:
        return (
            f"{self._buffer._comment_prefix} {self._message_key}: {self._text.format(**self._kwargs)} {self._buffer._comment_suffix}\n"+
            f"{self._buffer._comment_prefix}  - {self._fix.format(**self._kwargs)} {self._buffer._comment_suffix}\n"+
            f"{self._buffer._comment_prefix}{self._buffer._comment_suffix}"
        )

    def __str__(self) -> str:
        return self.render()


class _RenderLine:
    def __init__(
            self,
            buffer: "RenderBuffer",
            text: str,
            comment: bool = False
        ) -> None:
        self._buffer = buffer
        self._text = text
        self._is_comment = comment

    def render(self) -> str:
        if self._is_comment:
            return f"{self._buffer._comment_prefix} {self._text} {self._buffer._comment_suffix}"

        return self._text

    def __str__(self) -> str:
        return self.render()


class RenderBuffer:
    def __init__(self):
        self._lines: List[_RenderLine] = []
        self._debugs: List[_RenderMessage] = []
        self._warnings: List[_RenderMessage] = []
        self._errors: List[_RenderMessage] = []

        self._comment_prefix: str = "#"
        self._comment_suffix: str = ""
        self._empty = " "

        self._level_map: Mapping[MESSAGE_LEVELS, List[_RenderMessage]] = {
            "debug": self._debugs,
            "warning": self._warnings,
            "error": self._errors,
        }

    def get_message_list(self, level: MESSAGE_LEVELS) -> List[_RenderMessage]:
        message_list = self._level_map.get(level)
        if message_list is not None:
           return message_list

        raise ValueError(f"Invalid message level: {level}\nlevel must be one of following: `debug`, `info`, `warning`, `error`")

    def config_comment(self, prefix: str, suffix: str) -> None:
        self._comment_prefix = prefix
        self._comment_suffix = suffix

    def config_empty(self, empty) -> None:
        self._empty = empty

    def add_line(self, line: str, comment: bool = False) -> None:
        self._lines.append(_RenderLine(self, line, comment))

    def add_message(
            self,
            message_key: str,
            level: Optional[MESSAGE_LEVELS] = None,
            **kwargs: str,
        ) -> None:

        render_message = _RenderMessage(
            self,
            message_key,
            level,
            **kwargs
        )
        self.get_message_list(render_message._level).append(render_message)

    def add_empty(self) -> None:
        self.add_line(self._empty)

    def add_separator(self, name: str) -> None:
        self.add_line(f"--------> {name} <---------", comment=True)

    def render_lines(self) -> str:
        return "\n".join(line.render() for line in self._lines)

    def render_messages(self, level: MESSAGE_LEVELS) -> str:
        return "\n".join(msg.render() for msg in self.get_message_list(level))

    def render_all(self) -> str:
        sections = []

        if self._errors:
            self.config_comment("", "")
            sections.append(" ------------> Errors <------------ ")
            sections.append("")
            sections.append("The requested template cannot be rendered due to the following errors:")
            sections.append("")
            sections.append(self.render_messages("error"))

            if self._warnings:
                sections.append(" ------------> Warnings <------------ ")
                sections.append("")
                sections.append("Warnings while rendering the template:")
                sections.append("")
                sections.append(self.render_messages("warning"))

            sections.append("----------------------------------")

        else:
            p, s = self._comment_prefix, self._comment_suffix
            if DEBUG and self._debugs:
                sections.append(f"{p} ------------> Debug <------------ {s}")
                sections.append(f"{p}{s}")
                sections.append(f"{p} Debug messages while rendering the template: {s}")
                sections.append(f"{p}{s}")
                sections.append(self.render_messages("debug"))

            if self._warnings:
                sections.append(f"{p} ------------> Warnings <------------ {s}")
                sections.append(f"{p}{s}")
                sections.append(f"{p} Warnings while rendering the template: {s}")
                sections.append(f"{p}{s}")
                sections.append(self.render_messages("warning"))

            if sections:
                sections.append(f"{p} ---------------------------------- {s}")
                sections.append("")

            if self._lines:
                sections.append(self.render_lines())

        return "\n".join(sections)


__all__ = [
    "RenderBuffer",
]
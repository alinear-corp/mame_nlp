import io
from typing import Optional, Dict


DEFAULT_TARGETS = {
    "（": "）",
    "〔": "〕",
    "【": "】",
    "［": "］",
    "｛": "｝",
    "〈": "〉",
    "＜": "＞",
    "《": "》",
    "≪": "≫",
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


class ParenRemover:
    def __init__(
        self,
        targets: Optional[Dict[str, str]] = None,
        alt: str = "",
    ):
        if targets is None:
            targets = DEFAULT_TARGETS

        assert all(
            len(k) == 1 and len(v) == 1
            for k, v in targets.items()
        )
        self.targets = targets
        self.alt = alt

    def remove(self, text: str) -> str:
        stack = []
        buf = io.StringIO()

        last = 0
        for i, c in enumerate(text):
            close = self.targets.get(c)
            if close is not None:
                stack.append(close)
                buf.write(self.alt)
            elif len(stack) == 0:
                buf.write(c)
                last = i
            elif c == stack[-1]:
                stack.pop()
        if len(stack) > 0:
            stack.clear()
            buf.write(text[last + 1:])
        return buf.getvalue()

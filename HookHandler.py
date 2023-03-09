"""
在 hook 增加检测入口的 hook点处理类
"""


class HookHandler:
    _HEADER_KEY = "X-Protected-By"
    _HEADER_VALUE = "RASP"
    _REQUEST_ID_HEADER_KEY = "X-Request-ID"

def doCheck(type, params):
    pass


def doCheckWithoutRequest(type, params):
    pass

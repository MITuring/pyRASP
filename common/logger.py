import logging
from setting import setting
from setting.setting import Setting

loggers = {}
# 日志输出格式
LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(name)s] %(message)s'


class AgentLogger(object):
    def __init__(self, log):
        self._log = log

    def debug(self, msg, *args, **kwargs):
        return self._log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self._log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self._log.warning(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        return self._log.warn(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self._log.error(msg, args, kwargs)

    def exception(self, msg, *args, **kwargs):
        return self._log.exception(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        return self._log.log(level, msg, args, kwargs)


def logger_config(logging_name):
    global loggers

    if loggers.get(logging_name):
        return loggers.get(logging_name)

    setting = Setting()
    log_path = setting.log_path

    logger = logging.getLogger(logging_name)
    logger.handlers.clear()

    if setting.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logger.setLevel(level)

    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console)

    loggers[logging_name] = logger
    return AgentLogger(logger)
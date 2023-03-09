import functools
from abc import abstractmethod, ABCMeta
import HookContainer

print("absHook")


class AbstractModuleHook(metaclass=ABCMeta):
    _couldIgnore = True
    hook_name = ""
    HookContainer.hook_cls.update(hook_name)

    # hook 点所属检测类型
    @abstractmethod
    def getType(self):
        pass

    # 用于判断模块与当前需要hook的点是否相同
    @abstractmethod
    def isMatched(self, module_name):
        pass

    @abstractmethod
    def getMethodName(self):
        pass

    @abstractmethod
    def insertBefore(self):
        pass

    @abstractmethod
    def insertAfter(self):
        pass

    def transformModule(self, module):
        try:
            method_name = self.getMethodName()
            origin_method = getattr(module, method_name)
            module.__dict__[method_name] = self.func_wrapper(origin_method)
            return module
        except Exception:
            print("hook " + self.hook_name + " fail")

    def func_wrapper(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.insertBefore()
            result = func(*args, **kwargs)
            self.insertAfter()
            return result

        return wrapper

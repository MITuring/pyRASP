import importlib
import sys
import HookContainer


class MetaPathFinder:
    @staticmethod
    def find_module(fullname, path=None):
        print("find_module {}".format(fullname))
        return MetaPathLoader()


class MetaPathLoader:
    @staticmethod
    def load_module(fullname):
        print("load_module {}".format(fullname))
        finder = sys.meta_path.pop(0)
        module = importlib.import_module(fullname)
        HookContainer.module_hook(fullname, module)
        sys.meta_path.insert(0, finder)
        return module


sys.meta_path.insert(0, MetaPathFinder())

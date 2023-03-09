import inspect

has_hooked = []
hook_cls = []


def module_hook(fullname, module):
    for cls in hook_cls:
        if cls.isMatched(fullname):
            module = cls.transformModule(module)
            has_hooked.append(fullname)
    return module


# 调用链跟踪 Hook， Hook所有的模块的所有函数
def call_hooks(fullname, module):
    built_in_function = []
    module_cls = []
    builtin_members = inspect.getmembers(module, inspect.isbuiltin)
    module_cls = inspect.getmembers(module, inspect.isclass)
    for name in builtin_members:
        built_in_function.append(name[0])



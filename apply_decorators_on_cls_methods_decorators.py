from types import FunctionType
from utils.loggingUtils.lof import logger_decorator


def get_my_demand_method(cls):
    demand_methods = list()
    for method_name in dir(cls):
        method = getattr(cls, method_name)
        method_obj = cls.__dict__[method_name] if method_name in cls.__dict__ else method
        if isinstance(method_obj, staticmethod):
            demand_methods.append((method_name, method_obj, method, "staticmethod"))
        if isinstance(method_obj, classmethod):
            demand_methods.append((method_name, method_obj, method, "classmethod"))
        if isinstance(method_obj, FunctionType):
            demand_methods.append((method_name, method_obj, method, "FunctionType"))

    return demand_methods


def apply_decorators_on_cls_methods_decorators(*decorators_and_args: "(decorator_func, args,  kwargs)"):
    def prepare_wrapper(item, decorator_and_arg):
        decorator_func, dec_args, dec_kwargs = decorator_and_arg
        if item[3] == 'staticmethod':
            @staticmethod
            def wrapper(*args, **kwargs):
                return decorator_func(*dec_args, **dec_kwargs)(item[2])(*args, **kwargs)
        elif item[3] == 'classmethod':
            @classmethod
            def wrapper(cls, *args, **kwargs):
                return decorator_func(*dec_args, **dec_kwargs)(item[2])(*args, **kwargs)
        elif item[3] == 'FunctionType':
            def wrapper(self, *args, **kwargs):
                return decorator_func(*dec_args, **dec_kwargs)(item[2])(self, *args, **kwargs)

        return wrapper

    def inner_decorator(cls):
        name_obj_method = get_my_demand_method(cls)
        for item in name_obj_method:
            for decorator_and_arg in decorators_and_args:
                setattr(cls, item[0], prepare_wrapper(item, decorator_and_arg))
        return cls

    return inner_decorator


if __name__ == "__main__":
    # @apply_decorators_on_cls_methods_decorators((logger_decorator, (), {}))
    class SomeClass(object):
        def my_instanceMethod(self, p):
            print("instanceMethod: p = {}".format(p))

        @classmethod
        def my_classMethod(cls, p):
            print("classMethod: p = {}".format(p))

        @classmethod
        def my_classMethod2(cls, p):
            print("classMethod: p = {}".format(p))

        @staticmethod
        def my_staticMethod(p):
            print("staticMethod: p = {}".format(p))

        @staticmethod
        def my_staticMethod2(p):
            print("staticMethod: p = {}".format(p))


    instance = SomeClass()
    instance.my_instanceMethod(1)
    SomeClass.my_classMethod(2)
    instance.my_classMethod(2)
    SomeClass.my_staticMethod(3)
    instance.my_staticMethod(3)

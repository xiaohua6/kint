class cc(object):
    _is_instance=None
    def __new__(cls, *args, **kwargs):
        if cls._is_instance is None:
            cls._is_instance =super().__new__(cls)
        return cls._is_instance


bb=cc()
aa=cc()
print(id(bb),id(aa))


# def wraper():
#     def inner(dd):
#         if ndd.is_instanceot dd.is_instance:
#             dd.is_instance=dd.__new__()
#         return




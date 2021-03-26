class ExceptionLoadFail(Exception):
    def __init__(self,msg):
        super().__init__(self)
        self.msg = msg



def load_open_order(some):
    try:

        if some.startswith("hi"):
            return some
        else:
            raise ExceptionLoadFail("not a string.")
            return -1
    except Exception:
        import traceback
        traceback.print_exc()
        raise ExceptionLoadFail

load_open_order(None)
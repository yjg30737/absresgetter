import os
import inspect
import posixpath


def getabsres(res: str):
    stack_lst = inspect.stack()
    res_frame_idx = 0
    for i in range(len(stack_lst)):
        context = stack_lst[i].code_context[0]
        if context.find(res) == -1:
            pass
        else:
            res_frame_idx = i
    caller_path = os.path.dirname(stack_lst[res_frame_idx].filename)
    return os.path.join(caller_path, res).replace(os.path.sep, posixpath.sep)
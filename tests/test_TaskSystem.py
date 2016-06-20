
from nose.tools import assert_equal, assert_is, assert_is_not
from TaskSystem import *

import better_exchook
better_exchook.replace_traceback_format_tb()


def test_AsyncTask():
    def func(task):
        task.put(1)
        x = task.get()
        assert x == 2
    task = AsyncTask(func, name="test_AsyncTask")
    x = task.get()
    assert_equal(x, 1)
    task.put(2)
    task.join()

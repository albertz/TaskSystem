
from nose.tools import assert_equal, assert_is, assert_is_not
import TaskSystem
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


def test_AsyncTask_isFork():
    def func(task):
        assert TaskSystem.isFork
    task = AsyncTask(func, name="test_AsyncTask_isFork")
    task.join()
    assert not TaskSystem.isFork


def test_AsyncTask_ForwardedKeyboardInterrupt():
    def func(task):
        pass
    task = AsyncTask(func, name="test_AsyncTask_ForwardedKeyboardInterrupt")
    try:
        task.get()
        raise Exception("Did not get an exception.")
    except ProcConnectionDied:
        pass


def test_AsyncTask_mustExec():
    def func(task):
        assert not TaskSystem.isFork
        task.put(1)
        x = task.get()
        assert x == 2
    task = AsyncTask(func, mustExec=True, name="test_AsyncTask_isFork")
    x = task.get()
    assert_equal(x, 1)
    task.put(2)
    task.join()

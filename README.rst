==========
TaskSystem
==========

This is a collection of utilities to execute tasks in subprocesses.
This is similar to the `Python multiprocessing module <https://docs.python.org/library/multiprocessing.html>`_
but it supports more options.
Specifially, in Python 2 on Unix/Linux/MacOSX, the ``multiprocessing`` module
will use ``fork()`` without ``execv()``.
There are many libraries which do not well support a forked process environment
or at least are not as well tested as in a fresh process environment.
Thus, we use ``fork()`` + ``execv()`` for the subprocess.
Note that in Python 3, this is also supported by the ``multiprocessing`` module
via `multiprocessing.set_start_method <https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method>`_:

.. code-block:: python

  multiprocessing.set_start_method('spawn')

TaskSystem is used by `Music player <https://github.com/albertz/music-player>`_.

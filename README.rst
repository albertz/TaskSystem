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

One usage example is the use of multiple GPUs in Theano where
you would spawn a separate process for each GPU.
This is explained `here <https://github.com/Theano/Theano/wiki/Using-Multiple-GPUs`_.

TaskSystem is used
by `Music player <https://github.com/albertz/music-player>`_
(`here <https://github.com/albertz/music-player/blob/master/src/TaskSystem.py>`_)
and by `RETURNN <https://github.com/rwth-i6/returnn>`_
(`here <https://github.com/rwth-i6/returnn/blob/master/TaskSystem.py>`_).

One dump of the code is `here on a Gist <https://gist.github.com/albertz/4177e40d41cb7f9f7c68>`_
but it will be copied to this repository soon.


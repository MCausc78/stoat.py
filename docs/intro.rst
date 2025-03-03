:orphan:

.. currentmodule:: pyvolt

.. _intro:

Introduction
============

This is the documentation for pyvolt, a library for Python to aid
in creating bots that utilize the Revolt API.

Prerequisites
-------------

pyvolt works with Python 3.10 or higher. Support for earlier versions of Python
is not provided. Python 2.7 or lower is not supported. Python 3.9 or lower is not supported.


.. _installing:

Installing
----------

You can get the library directly from GitHub: ::

    python3 -m pip install -U git+https://github.com/MCausc78/pyvolt@master

If you are using Windows, then the following should be used instead: ::

    py -3 -m pip install -U git+https://github.com/MCausc78/pyvolt@master


To get voice support, you should use ``pyvolt[voice]`` instead of ``pyvolt``, e.g. ::

    python3 -m pip install -U git+https://github.com/MCausc78/pyvolt@master#egg=pyvolt[voice,speed]

Remember to check your permissions!

Virtual Environments
~~~~~~~~~~~~~~~~~~~~

Sometimes you want to keep libraries from polluting system installs or use a different version of
libraries than the ones installed on the system. You might also not have permissions to install libraries system-wide.
For this purpose, the standard library as of Python 3.3 comes with a concept called "Virtual Environment"s to
help maintain these separate versions.

A more in-depth tutorial is found on :doc:`py:tutorial/venv`.

However, for the quick and dirty:

1. Go to your project's working directory:

    .. code-block:: shell

        $ cd your-bot-source
        $ python3 -m venv bot-env

2. Activate the virtual environment:

    .. code-block:: shell

        $ source bot-env/bin/activate

    On Windows you activate it with:

    .. code-block:: shell

        $ bot-env\Scripts\activate.bat

3. Use pip like usual:

    .. code-block:: shell

        $ pip install -U git+https://github.com/MCausc78/pyvolt@master

Congratulations. You now have a virtual environment all set up.

.. note::

    Scripts executed with ``py -3`` will ignore any currently active virtual
    environment, as the ``-3`` specifies a global scope.

Basic Concepts
--------------

pyvolt revolves around the concept of :ref:`events <revolt-api-events>`.
An event is something you listen to and then respond to. For example, when a message
happens, you will receive an event about it that you can respond to.

A quick example to showcase how events work:

.. code-block:: python3

    import pyvolt

    class MyClient(pyvolt.Client):
        __slots__ = ()
        
        async def on_ready(self, event, /):
            print(f'Logged on as {event.me.tag}!')

        async def on_message(self, message, /):
            print(f'Message from {message.author}: {message.content}')

    client = MyClient()
    client.run('my token goes here')

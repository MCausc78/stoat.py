:orphan:

.. currentmodule:: stoat

.. _faq:

Frequently Asked Questions
==========================

This is a list of Frequently Asked Questions regarding using ``stoat.py`` and its extension modules. Feel free to suggest a
new question or submit one via pull requests.

.. contents:: Questions
    :local:
    :class: this-will-duplicate-information-and-it-is-still-useful-here

Coroutines
----------

Questions regarding coroutines and asyncio belong here.

What is a coroutine?
~~~~~~~~~~~~~~~~~~~~

A |coroutine_link|_ is a function that must be invoked with ``await`` or ``yield from``. When Python encounters an ``await`` it stops
the function's execution at that point and works on other things until it comes back to that point and finishes off its work.
This allows for your program to be doing multiple things at the same time without using threads or complicated
multiprocessing.

**If you forget to await a coroutine then the coroutine will not run. Never forget to await a coroutine.**

Where can I use ``await``\?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can only use ``await`` inside ``async def`` functions and nowhere else.

General
-------

General questions regarding library usage belong here.

Why my :attr:`stoat.Server.members` is empty/does not match reality?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You either disabled member cache, or did not setup chunking. See `this page <ext/chunking/index>` for how to do this.

Why :attr:`stoat.Client.servers` is empty when I access it through :class:`~stoat.ReadyEvent`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike discord.py, this library does not populate cache during dispatching an event. Consider using
:attr:`stoat.ReadyEvent.servers` to retrieve servers in :class:`~stoat.ReadyEvent`.
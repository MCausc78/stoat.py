.. pyvolt documentation master file, created by
   sphinx-quickstart on Sat Dec  7 15:53:41 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyvolt
=================

pyvolt is a modern, easy to use, feature-rich, and async ready API wrapper
for the Revolt bot and user APIs.

**Features:**

- Modern Pythonic API using ``async``\/``await`` syntax
- Sane rate limit handling that prevents 429s
- Command extension to aid with bot creation
- Easy to use with an object oriented design
- Optimized for both speed and memory
- Flexible

Getting Started
---------------

Is this your first time using the library? This is the place to get started!

- **First steps:** :doc:`intro` | :doc:`quickstart` | :doc:`logging`
- **Working with Revolt:** :doc:`authenticating` | :doc:`revolt` | :doc:`server_subscriptions`
- **Examples:** Many examples are available in the :resource:`repository <examples>`

Getting help
------------

If you're having trouble with something, these resources might help.

- Try the :doc:`faq` first, it's got answers to all common questions.
- Ask us and hang out with us in our :resource:`Revolt <revolt>` server.
- If you're looking for something specific, try the :ref:`index <genindex>` or :ref:`searching <search>`.
- Report bugs in the :resource:`issue tracker <issues>`.
- Ask in our :resource:`GitHub discussions page <discussions>`.

Extensions
----------

These extensions help you during development when it comes to common tasks.

.. toctree::
  :maxdepth: 1

  ext/chunking/index.rst
  ext/commands/index.rst

Manuals
-------

These pages go into great detail about everything the API can do.

.. toctree::
  :maxdepth: 1

  API reference <api/index.rst>
  pyvolt.ext.chunking API reference <ext/chunking/api.rst>
  pyvolt.ext.commands API reference <ext/commands/api.rst>
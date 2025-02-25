.. _pyvolt_ext_chunking:

``pyvolt.ext.chunking`` -- An extension for member chunking
===========================================================

While ``pyvolt`` offers a lower level aspect on interacting with Revolt, it does not provide automated member chunking.
Generally it's unnecessary boilerplate since it's a simple aspect, but hard to get correctly while being flexible.
For this reason, ``pyvolt`` comes with it's own extension to handle this.


.. toctree::
    :maxdepth: 2

    api

Example
-------

.. code:: py

    from pyvolt.ext.chunking import MemberChunker

    MemberChunker(bot)

That's it. Now the cache will be always populated.
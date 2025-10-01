.. _stoat_ext_chunking:

``stoat.ext.chunking`` -- An extension for member chunking
===========================================================

While ``stoat.py`` offers a lower level aspect on interacting with Stoat, it does not provide automated member chunking.
Generally it's unnecessary boilerplate since it's a simple aspect, but hard to get correctly while being flexible.
For this reason, ``stoat.py`` comes with it's own extension to handle this.


.. toctree::
    :maxdepth: 2

    api

Example
-------

.. code:: py

    from stoat.ext.chunking import MemberChunker

    MemberChunker(bot)

That's it. Now the cache will be always populated.

.. note::
    
    If passing ``flags`` parameter to constructor, make sure you have :attr:`~stoat.ext.chunking.MemberChunkerFlags.subscribe_to_events` flag.

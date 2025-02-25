.. currentmodule:: pyvolt

API Reference
=============

The following section outlines the API of pyvolt's chunking extension module.

.. _ext_chunking_api_member_chunker:

Member Chunking
---------------

MemberChunker
~~~~~~~~~~~~~

.. attributetable:: pyvolt.ext.chunking.MemberChunker

.. autoclass:: pyvolt.ext.chunking.MemberChunker
    :members:

MemberChunkerFlags
~~~~~~~~~~~~~~~~~~

.. attributetable:: pyvolt.ext.chunking.MemberChunkerFlags

.. autoclass:: pyvolt.ext.chunking.MemberChunkerFlags
    :members:

MemberChunkingStrategy
~~~~~~~~~~~~~~~~~~~~~~

.. class:: MemberChunkingStrategy

    Strategy how to chunk server members.
    
    .. attribute:: normal
        
        Chunk prioritized servers first, then chunk rest of servers.
    .. attribute:: defer_prioritized
        
        Chunk prioritized servers last, after chunking all of unprioritized servers.

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

    Represents a strategy to chunk server members.
    
    .. attribute:: normal
        
        Chunk servers normally.
    .. attribute:: defer_prioritized
        
        Defer prioritized servers.

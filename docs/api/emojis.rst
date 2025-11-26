.. currentmodule:: stoat

Emojis
======

The following section documents everything related to emojis.

Models
------

BaseEmoji
~~~~~~~~~

.. attributetable:: BaseEmoji

.. autoclass:: BaseEmoji
    :members:
    :inherited-members:

ServerEmoji
~~~~~~~~~~~

.. attributetable:: ServerEmoji

.. autoclass:: ServerEmoji
    :members:
    :inherited-members:

DetachedEmoji
~~~~~~~~~~~~~

.. attributetable:: DetachedEmoji

.. autoclass:: DetachedEmoji
    :members:
    :inherited-members:

Emoji
~~~~~

.. class:: Emoji

    An union of all emoji types.

    The following classes are included in this union:
    
    - :class:`.ServerEmoji`
    - :class:`.DetachedEmoji`

ResolvableEmoji
~~~~~~~~~~~~~~~

.. class:: ResolvableEmoji

    An union of either :class:`.BaseEmoji` or :class:`str` (which is either unicode emoji or emoji ID).

.. autofunction:: resolve_emoji

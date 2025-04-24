.. currentmodule:: pyvolt

Embeds
======

The following section documents everything related to embeds. Embeds usually can be found inside messages.

Models
------

BaseEmbed
~~~~~~~~~

.. attributetable:: BaseEmbed

.. autoclass:: BaseEmbed
    :members:

BaseEmbedSpecial
~~~~~~~~~~~~~~~~

.. attributetable:: BaseEmbedSpecial

.. autoclass:: BaseEmbedSpecial
    :members:

NoneEmbedSpecial
~~~~~~~~~~~~~~~~

.. attributetable:: NoneEmbedSpecial

.. autoclass:: NoneEmbedSpecial
    :members:
    :inherited-members:

GIFEmbedSpecial
~~~~~~~~~~~~~~~

.. attributetable:: GIFEmbedSpecial

.. autoclass:: GIFEmbedSpecial
    :members:
    :inherited-members:

YouTubeEmbedSpecial
~~~~~~~~~~~~~~~~~~~

.. attributetable:: YouTubeEmbedSpecial

.. autoclass:: YouTubeEmbedSpecial
    :members:
    :inherited-members:

LightspeedEmbedSpecial
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: LightspeedEmbedSpecial

.. autoclass:: LightspeedEmbedSpecial
    :members:
    :inherited-members:

TwitchEmbedSpecial
~~~~~~~~~~~~~~~~~~

.. attributetable:: TwitchEmbedSpecial

.. autoclass:: TwitchEmbedSpecial
    :members:
    :inherited-members:

SpotifyEmbedSpecial
~~~~~~~~~~~~~~~~~~~

.. attributetable:: SpotifyEmbedSpecial

.. autoclass:: SpotifyEmbedSpecial
    :members:
    :inherited-members:

SoundcloudEmbedSpecial
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SoundcloudEmbedSpecial

.. autoclass:: SoundcloudEmbedSpecial
    :members:
    :inherited-members:

BandcampEmbedSpecial
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BandcampEmbedSpecial

.. autoclass:: BandcampEmbedSpecial
    :members:
    :inherited-members:

AppleMusicEmbedSpecial
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AppleMusicEmbedSpecial

.. autoclass:: AppleMusicEmbedSpecial
    :members:
    :inherited-members:

StreamableEmbedSpecial
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StreamableEmbedSpecial

.. autoclass:: StreamableEmbedSpecial
    :members:
    :inherited-members:

ImageEmbed
~~~~~~~~~~

.. attributetable:: ImageEmbed

.. autoclass:: ImageEmbed
    :members:
    :inherited-members:

VideoEmbed
~~~~~~~~~~

.. attributetable:: VideoEmbed

.. autoclass:: VideoEmbed
    :members:
    :inherited-members:

WebsiteEmbed
~~~~~~~~~~~~

.. attributetable:: WebsiteEmbed

.. autoclass:: WebsiteEmbed
    :members:
    :inherited-members:

StatelessTextEmbed
~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessTextEmbed

.. autoclass:: StatelessTextEmbed
    :members:
    :inherited-members:

TextEmbed
~~~~~~~~~

.. attributetable:: TextEmbed

.. autoclass:: TextEmbed
    :members:
    :inherited-members:

NoneEmbed
~~~~~~~~~

.. attributetable:: NoneEmbed

.. autoclass:: NoneEmbed
    :members:
    :inherited-members:

EmbedSpecial
~~~~~~~~~~~~

.. class:: EmbedSpecial

    An union of all embed special types.

    The following classes are included in this union:
    
    - :class:`.GIFEmbedSpecial`
    - :class:`.YouTubeEmbedSpecial`
    - :class:`.LightspeedEmbedSpecial`
    - :class:`.TwitchEmbedSpecial`
    - :class:`.SpotifyEmbedSpecial`
    - :class:`.SoundcloudEmbedSpecial`
    - :class:`.BandcampEmbedSpecial`
    - :class:`.AppleMusicEmbedSpecial`
    - :class:`.StreamableEmbedSpecial`

StatelessEmbed
~~~~~~~~~~~~~~

.. class:: StatelessEmbed

    An union of all stateless embed types.

    The following classes are included in this union:
    
    - :class:`.WebsiteEmbed`
    - :class:`.ImageEmbed`
    - :class:`.VideoEmbed`
    - :class:`.StatelessTextEmbed`
    - :class:`.NoneEmbed`

Embed
~~~~~

.. class:: Embed

    An union of all embed types.

    The following classes are included in this union:
    
    - :class:`.WebsiteEmbed`
    - :class:`.ImageEmbed`
    - :class:`.VideoEmbed`
    - :class:`.TextEmbed`
    - :class:`.NoneEmbed`

SendableEmbed
~~~~~~~~~~~~~

.. autoclass:: SendableEmbed
    :members:
.. currentmodule:: pyvolt

Enums and Flag Classes
======================

The following section documents everything related to enums and flags.

.. _revolt-api-enums:

Enumerations
------------

The API provides some enumerations for certain types of strings to avoid the API
from being stringly typed in case the strings change in the future.

All enumerations are subclasses of a custom class which mimics the behavior
of :class:`enum.Enum`.

Enum
~~~~

.. attributetable:: Enum

.. autoclass:: Enum
    :members:

Authentication
~~~~~~~~~~~~~~

.. class:: MFAMethod

    Specifies the method of MFA.
    
    .. attribute:: password

        The MFA is being done using password.
    .. attribute:: recovery

        The MFA is being done using recovery code.
    .. attribute:: totp

        The MFA is being done using TOTP code.

Asset
~~~~~

.. class:: AssetMetadataType

    Specifies the metadata type of asset.

    .. attribute:: file

        The file is just a generic uncategorized file.
    .. attribute:: text

        The file contains textual data and should be displayed as such.
    .. attribute:: image

        The file is an image with specific dimensions.
    .. attribute:: video

        The file is a video with specific dimensions.
    .. attribute:: audio

        The file is audio.

Channel
~~~~~~~

.. class:: ChannelType
    
    Specifies the type of a channel.

    .. attribute:: saved_messages
        
        A channel accessible only to one user.
    .. attribute:: private

        A private text channel. Also called a direct message.
    .. attribute:: group
        
        A private group text channel.
    .. attribute:: text

        A text channel.
    .. attribute:: voice

        A voice channel.
    .. attribute:: unknown

        The channel type is unknown.

Discover
~~~~~~~~

.. class:: BotUsage

    Specifies bot's usage.
    
    .. attribute:: high

        Bot is actively used.
    .. attribute:: medium

        Bot is used but not frequently.
    .. attribute:: low

        Bot is frequently unused.

.. class:: ServerActivity

    Specifies server activity.
    
    .. attribute:: high

        Server is highly active.
    .. attribute:: medium

        Server is active.
    .. attribute:: low

        Server has too low activity.
    .. attribute:: no

        Server has no activity at all.

Embeds
~~~~~~

.. class:: BandcampContentType

    Specifies type of remote Bandcamp content.

    .. attribute:: album
        
        A Bandcamp album.
    .. attribute:: track

        A Bandcamp track.

.. class:: ImageSize

    Specifies image positioning and size.

    .. attribute:: large
        
        Show large preview at the bottom of the embed.
    .. attribute:: preview

        Show small preview to the side of the embed.

.. class:: LightspeedContentType

    Specifies type of remote Lightspeed.tv content.

    .. attribute:: channel
        
        A Lightspeed.tv channel.

.. class:: TwitchContentType
    
    Specifies type of remote Twitch content.

    .. attribute:: channel
        
        A Twitch channel.
    .. attribute:: video
        
        A Twitch video.
    .. attribute:: clip
        
        A Twitch clip.

Messages
~~~~~~~~

.. class:: MessageSort
    
    Specifies order of messages.

    .. attribute:: relevance

        Sort messages by relevance.
    .. attribute:: latest
        
        Sort messages by timestamp in descending order.
    .. attribute:: oldest

        Sort messages by timestamp in ascending order.

OAuth2
~~~~~~

.. class:: OAuth2ResponseType

    Specifies what ``code`` querystring parameter in resulting OAuth2 redirect URL will contain.

    .. attribute:: code

        The parameter will contain code that should be exchanged.
    .. attribute:: token

        The parameter will contain OAuth2 token.

.. class:: OAuth2GrantType

    Specifies the grant type of OAuth2 flow.

    .. attribute:: authorization_code

        The client will have to ask server to exchange code.
    .. attribute:: implicit

        The client will receive OAuth2 token directly.

.. class:: OAuth2CodeChallengeMethod

    Specifies the method of generating OAuth2 code challenge.
    
    .. attribute:: plain

        The code challenge will be provided as-is.
    .. attribute:: s256

        The code challenge will be hashed using :func:`SHA256 <hashlib.sha256>`.

.. class:: OAuth2Scope

    Specifies the scope(s) of OAuth2 token.
    
    .. attribute:: identify

        The token can be used to :meth:`retrieve user's information and friends <HTTPClient.get_me>`.
    .. attribute:: servers

        The token can be used to :meth:`retrieve user's servers <HTTPClient.get_servers>`.
    .. attribute:: upload_files

        The token can be used to upload files.
    .. attribute:: events

        The token can be used to connect to Gateway on user's behalf.
    .. attribute:: full

        The token can be used to access entire Revolt HTTP API.

Reporting
~~~~~~~~~

.. class:: ContentReportReason

    Specifies reason for reporting message or a server.
    
    .. attribute:: none
        
        No reason has been specified.
    .. attribute:: illegal
    
        Illegal content catch-all reason.
    .. attribute:: illegal_goods
    
        Server or user is selling or facilitating use of drugs or other illegal goods.
    .. attribute:: illegal_extortion
    
        Extortion or blackmail.
    .. attribute:: illegal_pornography
    
        Revenge or child pornography.
    .. attribute:: illegal_hacking
    
        Illegal hacking activity.
    .. attribute:: extreme_violence
    
        Extreme violence, gore, or animal cruelty, with exception to violence potrayed in media / creative arts.
    .. attribute:: promotes_harm
    
        Content that promotes harm to others / self.
    .. attribute:: unsolicited_spam
    
        Unsolicited advertisements.
    .. attribute:: raid
    
        Server or user is raiding.
    .. attribute:: spam_abuse
    
        Server or user is spamming or doing other sort of platform abuse.
    .. attribute:: scams_fraud
    
        Server is scamming or doing fraud.
    .. attribute:: malware
    
        Server or user is distributing malware or malicious links.
    .. attribute:: harassment
    
        Harassment or abuse targeted at another user.

.. class:: ReportStatus

    Specifies the status of a report.

    .. attribute:: created
        
        The report was just created and pending.
    .. attribute:: rejected

        The report was rejected.
    .. attribute:: resolved

        The report was resolved.

.. class:: ReportedContentType

    Specifies the type of reported content.

    .. attribute:: message

        The content being reported is message.
    .. attribute:: server

        The content being reported is server.
    .. attribute:: user

        The content being reported is user.

Servers
~~~~~~~

.. class:: MemberRemovalIntention
    
    Specifies reason why member was removed from server.

    .. attribute:: leave

        The member manually left.
    .. attribute:: kick

        The member was kicked.
    .. attribute:: ban

        The member was banned.

Settings
~~~~~~~~

.. class:: Language

    Specifies language.

    .. attribute:: english

        English (Traditional)
    .. attribute:: english_simplified

        English (Simplified)
    .. attribute:: arabic

        عربي
    .. attribute:: assamese

        অসমীয়া
    .. attribute:: azerbaijani

        Azərbaycan dili
    .. attribute:: belarusian

        Беларуская
    .. attribute:: bulgarian

        Български
    .. attribute:: bengali

        বাংলা
    .. attribute:: breton

        Brezhoneg
    .. attribute:: catalonian

        Català
    .. attribute:: cebuano

        Bisaya
    .. attribute:: central_kurdish

        کوردی
    .. attribute:: czech

        Čeština
    .. attribute:: danish

        Dansk
    .. attribute:: german

        Deutsch
    .. attribute:: greek

        Ελληνικά
    .. attribute:: spanish

        Español
    .. attribute:: spanish_latin_america

        Español (América Latina)
    .. attribute:: estonian

        eesti
    .. attribute:: finnish

        suomi
    .. attribute:: filipino

        Filipino
    .. attribute:: french

        Français
    .. attribute:: irish

        Gaeilge
    .. attribute:: hindi

        हिन्दी
    .. attribute:: croatian

        Hrvatski
    .. attribute:: hungarian

        Magyar
    .. attribute:: armenian

        հայերեն
    .. attribute:: indonesian

        Bahasa Indonesia
    .. attribute:: icelandic

        Íslenska
    .. attribute:: italian

        Italiano
    .. attribute:: japense

        日本語
    .. attribute:: korean

        한국어
    .. attribute:: luxembourgish

        Lëtzebuergesch
    .. attribute:: lithuanian

        Lietuvių
    .. attribute:: latvian

        Latviešu
    .. attribute:: macedonian

        Македонски
    .. attribute:: malay

        Bahasa Melayu
    .. attribute:: norwegian_bokmal

        Norsk bokmål
    .. attribute:: dutch

        Nederlands
    .. attribute:: persian

        فارسی
    .. attribute:: polish

        Polski
    .. attribute:: portuguese_brazil

        Português (do Brasil)
    .. attribute:: portuguese_portugal

        Português (Portugal)
    .. attribute:: romanian

        Română
    .. attribute:: russian

        Русский
    .. attribute:: slovak

        Slovensky
    .. attribute:: slovenian

        Slovenščina
    .. attribute:: albanian

        Shqip
    .. attribute:: serbian

        Српски
    .. attribute:: sinhalese

        සිංහල
    .. attribute:: swedish

        Svenska
    .. attribute:: tamil

        தமிழ்
    .. attribute:: thai

        ไทย
    .. attribute:: turkish

        Türkçe
    .. attribute:: urdu

        اردو
    .. attribute:: ukrainian

        Українська
    .. attribute:: venetian

        Vèneto
    .. attribute:: vietnamese

        Tiếng Việt
    .. attribute:: chinese_simplified

        简体中文
    .. attribute:: chinese_traditional

        繁體中文
    .. attribute:: tokipona

        Toki Pona
    .. attribute:: esperanto

        Esperanto
    .. attribute:: owo

        OwO

        .. note::
            This is joke language.
    .. attribute:: pirate

        Pirate

        .. note::
            This is joke language.
    .. attribute:: bottom

        Bottom

        .. note::
            This is joke language.
    .. attribute:: leet

        1337
        
        .. note::
            This is joke language.
    .. attribute:: piglatin

        Pig Latin
        
        .. note::
            This is joke language.
    .. attribute:: enchantment_table

        Enchantment Table
        
        .. note::
            This is joke language.

.. class:: AndroidTheme

    Specifies client theme for Revolt Android.

    .. attribute:: revolt
        
        Use Revolt colors.
    .. attribute:: light
        
        Represents the Light theme on Revolt Android.
    .. attribute:: pure_black
        
        Represents the AMOLED theme on Revolt Android.
    .. attribute:: system
        
        Use system theme.
    .. attribute:: material_you
        
        Represents the Material You theme on Revolt Android.

.. class:: AndroidProfilePictureShape

    Specifies rounding grade for profile pictures, including in chat and profiles.
    This applies to all users on Revolt Android.

    .. attribute:: sharp
    
        Use sharp rounding grade for profile pictures.
    .. attribute:: rounded

        Use rounded grade for profile pictures.
    .. attribute:: circular

        Use circular rounding grade for profile pictures.

.. class:: AndroidMessageReplyStyle

    Specifies a way to quickly reply on Revolt Android.

    .. attribute:: long_press_to_reply

        Long press message to reply.
    .. attribute:: swipe_to_reply

        Swipe from message end to reply.
    .. attribute:: double_tap_to_reply

        Tap twice a message to reply.

.. class:: ReviteChangelogEntry

    Represents a Revite changelog entry.

    More details about entries may be found `here <https://github.com/revoltchat/revite/blob/478d3751255a441bf39057b81f807ffe96a0e97a/src/assets/changelogs.tsx>`_.

    .. attribute:: mfa_feature
        
        Represents a changelog entry about securing accounts with MFA.
    .. attribute:: iar_reporting_feature

        Represents a changelog entry about in-app reporting messages, servers and users.
    .. attribute:: discriminators_feature
        
        Represents a changelog entry about adding discriminators.
    .. property:: created_at

        When the changelog entry was created.
    .. property:: title

        The changelog entries' title.

.. class:: ReviteNotificationState

    Specifies the notification's state.
    
    .. attribute:: all_messages

        You're always notified unless you're busy.
    .. attribute:: mentions_only

        You're only notified on mentions unless you're busy.
    .. attribute:: none

        State is not specified. Currently same as :attr:`.muted`.
    .. attribute:: muted

        The channel/server is muted.

.. class:: ReviteEmojiPack

    Specifies the emoji pack to render.

    .. attribute:: mutant_remix

        Use 'Mutant Remix' emoji pack.
    .. attribute:: twemoji

        Use 'Twemoji' emoji pack.
    .. attribute:: openmoji

        Use 'Openmoji' emoji pack.
    .. attribute:: noto_emoji

        Use 'Noto Emoji' emoji pack.

.. class:: ReviteBaseTheme

    Represents the Revite client theme.

    .. attribute:: light
        
        Represents the Light theme on Revolt.
    .. attribute:: dark
        
        Represents the Dark theme on Revolt.

.. class:: ReviteFont
    
    Specifies the font in Revite client.
    
    .. attribute:: open_sans

        Represents 'Open Sans' font.
    .. attribute:: opendyslexic
        
        Represents 'OpenDyslexic' font.
    .. attribute:: inter
        
        Represents 'Inter' font.

        .. note::
            This font supports ligatures.
    .. attribute:: atkinson_hyperlegible
        
        Represents 'Atkinson Hyperlegible' font.
    .. attribute:: roboto
        
        Represents 'Roboto' font.
    .. attribute:: noto_sans
        
        Represents 'Noto Sans' font.
    .. attribute:: lato
        
        Represents 'Lato' font.
    .. attribute:: bitter
        
        Represents 'Bitter' font.
    .. attribute:: montserrat
        
        Represents 'Montserrat' font.
    .. attribute:: poppins
        
        Represents 'Poppins' font.
    .. attribute:: raleway
        
        Represents 'Raleway' font.
    .. attribute:: ubuntu
        
        Represents 'Ubuntu' font.
    .. attribute:: comic_neue
        
        Represents 'Comic Neue' font.
    .. attribute:: lexend
        
        Represents 'Lexend' font.

.. class:: ReviteMonoFont
    
    Specifies the font inside codeblocks in Revite client.
    
    .. attribute:: fira_code
        
        Represents 'Fira Code' mont.
    .. attribute:: roboto_mono
        
        Represents 'Roboto Mono' mont.
    .. attribute:: source_code_pro
        
        Represents 'Source Code Pro' mont.
    .. attribute:: space_mono
        
        Represents 'Space Mono' mont.
    .. attribute:: ubuntu_mono
        
        Represents 'Ubuntu Mono' mont.
    .. attribute:: jetbrains_mono
        
        Represents 'JetBrains Mono' mont.

Shard
~~~~~

.. class:: ShardFormat

    Specifies WebSocket format the shard should communicate in.
    
    .. attribute:: json
        
        Communicate using JSON.
        
        Recommended for testing.
    .. attribute:: msgpack

        Communicate using `MessagePack <https://msgpack.org/index.html>`_ format.

        Recommended for production due to being most efficient format.

Users
~~~~~

.. class:: Presence
    
    Specifies the presence of an user.

    .. attribute:: online

        The user is online.
    .. attribute:: idle

        The user is currently not available.
    .. attribute:: focus

        The user is focusing and will only receive mentions.
    .. attribute:: busy

        The user is busy and will not receive any notifications.
    .. attribute:: invisible
        The user appears to be offline to other users.

.. class:: RelationshipStatus

    Specifies the relationship of current user and another user (or themselves).

    .. attribute:: none
        
        No relationship.
    .. attribute:: user
        
        This user is you.
    .. attribute:: friend
        
        This user is friends with you.
    .. attribute:: outgoing

        You sent friend request to this user.
    .. attribute:: incoming

        This user sent friend request to you.
    .. attribute:: blocked
        
        You blocked this user.
    .. attribute:: blocked_other

        This user blocked you.

.. class:: UserReportReason

    Specifies reason for user report.

    .. attribute:: none

        No reason has been specified.
    .. attribute:: unsolicited_spam

        User is sending unsolicited advertisements.
    .. attribute:: spam_abuse

        User is sending spam or abusing the platform.
    .. attribute:: inappropriate_profile

        User's profile contains inappropriate content for a general audience.
    .. attribute:: impersonation

        User is impersonating another user.
    .. attribute:: ban_evasion

        User is evading a ban.
    .. attribute:: underage

        User is not of minimum age to use the platform.

.. _revolt-api-flags:

Flag Classes
------------

BaseFlags
~~~~~~~~~

.. attributetable:: BaseFlags

.. autoclass:: BaseFlags
    :members:

.. autofunction:: flag

.. autofunction:: doc_flags

BotFlags
~~~~~~~~

.. attributetable:: BotFlags

.. autoclass:: BotFlags
    :members:
    :inherited-members:

MessageFlags
~~~~~~~~~~~~

.. attributetable:: MessageFlags

.. autoclass:: MessageFlags
    :members:
    :inherited-members:

Permissions
~~~~~~~~~~~

.. attributetable:: Permissions

.. autoclass:: Permissions
    :members:
    :inherited-members:

.. data:: ALLOW_PERMISSIONS_IN_TIMEOUT

    The permissions that are only allowed when user is timed out.
.. data:: VIEW_ONLY_PERMISSIONS

    The permissions that are allowed when user can view channel.
.. data:: DEFAULT_PERMISSIONS

    The default permissions.
.. data:: DEFAULT_SAVED_MESSAGES_PERMISSIONS

    The default permissions in :class:`.SavedMessagesChannel`.
.. data:: DEFAULT_DM_PERMISSIONS

    The default permissions in :class:`.DMChannel`.
.. data:: DEFAULT_SERVER_PERMISSIONS

    The default permissions in :class:`.Server`.

UserPermissions
~~~~~~~~~~~~~~~

.. attributetable:: UserPermissions

.. autoclass:: UserPermissions
    :members:
    :inherited-members:

ServerFlags
~~~~~~~~~~~

.. attributetable:: ServerFlags

.. autoclass:: ServerFlags
    :members:
    :inherited-members:

UserBadges
~~~~~~~~~~

.. attributetable:: UserBadges

.. autoclass:: UserBadges
    :members:
    :inherited-members:

UserFlags
~~~~~~~~~

.. attributetable:: UserFlags

.. autoclass:: UserFlags
    :members:
    :inherited-members:
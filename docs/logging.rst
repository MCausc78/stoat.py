:orphan:

.. currentmodule:: stoat
.. _logging_setup:

Setting Up Logging
==================

*stoat.py* logs errors and debug information via the :mod:`logging` Python
module. In order to streamline this process, the library provides default configuration for the ``stoat`` logger when using :meth:`Client.run`. It is strongly recommended that the logging module is configured, as no errors or warnings will be output if it is not set up.

The default logging configuration provided by the library will print to :data:`sys.stderr` using coloured output. You can configure it to send to a file instead by using one of the built-in :mod:`logging.handlers`, such as :class:`logging.FileHandler`.

This can be done by passing it through :meth:`Client.run`:

.. code-block:: python3

    import logging

    handler = logging.FileHandler(filename='stoat.log', encoding='utf-8', mode='w')

    # Assume client refers to a stoat.Client subclass...
    client.run(token, log_handler=handler)

You can also disable the library's logging configuration completely by passing ``None``:

.. code-block:: python3

    client.run(token, log_handler=None)


Likewise, configuring the log level to ``logging.DEBUG`` is also possible:

.. code-block:: python3

    import logging

    handler = logging.FileHandler(filename='stoat.log', encoding='utf-8', mode='w')

    # Assume client refers to a stoat.Client subclass...
    client.run(token, log_handler=handler, log_level=logging.DEBUG)

This is recommended, especially at verbose levels such as ``DEBUG``, as there are a lot of events logged and it would clog the stderr of your program.

If you want the logging configuration the library provides to affect all loggers rather than just the ``stoat`` logger, you can pass ``root_logger=True`` inside :meth:`Client.run`:

.. code-block:: python3

    client.run(token, log_handler=handler, root_logger=True)

If you want to setup logging using the library provided configuration without using :meth:`Client.run`, you can use :func:`stoat.utils.setup_logging`:

.. code-block:: python3

    import stoat

    stoat.utils.setup_logging()

    # or, for example
    stoat.utils.setup_logging(level=logging.INFO, root=False)

More advanced setups are possible with the :mod:`logging` module. The example below configures a rotating file handler that outputs DEBUG output for everything the library outputs, except for HTTP requests:

.. code-block:: python3

    import stoat
    import logging
    import logging.handlers

    logger = logging.getLogger('stoat')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('stoat.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='stoat.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Assume client refers to a stoat.Client subclass...
    # Suppress the default configuration since we have our own
    client.run(token, log_handler=None)


For more information, check the documentation and tutorial of the :mod:`logging` module.

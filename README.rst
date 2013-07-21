===========
BASH UTILS
===========

Bash colors management and log system for python users

Bashutils provide you two functionnalities:

* Create bash colored text
* Log message system (like lsb init-functions log message)

**Imports** :

.. code-block:: console

    from bashutils import colors
    from bashutils import logmsg


bash colors
===========

**Imports** :

    from bashutils import colors


Color function :
``color_text(text, color="none", bcolor="none", effect="none")``

* color : text color
* bcolor : background color
* effect : font effect

**Text and background colors list** : none, black ,red ,green ,yellow ,blue ,magenta ,cyan ,white

*default color is 'none' (terminal default color)*


**Text effects** : none, bold, underscore, blink, reverse, concealed

*default effect is 'none'*

bash logmsg
===========

**Imports** :

    from bashutils import logmsg

Functions
---------

Basic functions
~~~~~~~~~~~~~~~

Start a new log message :

.. code-block:: console

    log_begin_message("My message")

End a log message :

.. code-block:: console

    log_end_message(logmsg.LOG.OK)

**Existing log type** : LOG.OK (0), LOG.FAIL (1), LOG.ERROR (2)

Predefined message (begin and end message):

.. code-block:: console

    log_success_msg("My message")
    log_failure_msg("My message")
    log_error_msg("My message")``


Other functions
~~~~~~~~~~~~~~~

If you want to add some information before or after the begin message, you can use these functions:

.. code-block:: console

    log_msg_pre("SUPP")
    log_msg_post("SUPP")
    log_end_msg_pre("SUPP", logmsg.LOG.OK)
    log_end_msg_post("SUPP", logmsg.LOG.OK)

*The last two functions add a PRE or POST information and end massage with LOG status*


Add a LOG Type
~~~~~~~~~~~~~~~

It is possible to add a new LOG Type :

.. code-block:: console

    add_log_type(name, display, color, bcolor)

* name : call name (A-Z and '_')
* display : display message in [-]
* color : text color (see bashutils.colors)
* bcolor : background color (see bashutils.colors)

You can use this new LOG with ``LOG.MYNEWLOG`` (name in upper case)

You have an all in one function like ``log_success_msg`` with :

.. code-block:: console

    log_msg_type("My message", logmsg.LOG.MYNEWLOG)

Example :

.. code-block:: console

    add_log_type("MYNEWLOG", "NEWL", "red", "yellow")
    log_msg_type("Message with new LOG", LOG.MYNEWLOG)

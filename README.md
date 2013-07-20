BASH UTILS
===========

Bash colors management and log system

Bashutils provide you two functionnalities:

* Create bash colored text
* Log message system (like lsb init-functions log message)

**Imports** :

    from bashutils import colors
    from bashutils import logmsg


bash colors
===========

Color function :
```color_text(text, color="none", bcolor="none", effect="none")```

* color : text color
* bcolor : background color
* effect : font effect

**Text and background colors list** : none, black ,red ,green ,yellow ,blue ,magenta ,cyan ,white

*default color is 'none' (terminal default color)*


**Text effects** : none, bold, underscore, blink, reverse, concealed

*default effect is 'none'*

bash logmsg
===========

Start a new log message :
```
log_begin_message("My message")
```

End a log message :
```
log_end_message(logmsg.LOG["OK"])
```

Log type : OK (0), FAIL (1), WARNING (2), ERROR (3)

Predefined message (begin and end message):
```
log_success_msg("My message")
log_failure_msg("My message")
log_error_msg("My message")
```

Predefined for all types :
```
log_msg_type("My message", logmsg.LOG["OK"])
```

Add pre or post information on log message :
```
log_msg_pre("SUPP")
log_msg_post("SUPP")
```

Add pre or post information on log message and end it :
```
log_end_msg_pre("SUPP", logmsg.LOG["OK"])
log_end_msg_post("SUPP", logmsg.LOG["OK"])
```

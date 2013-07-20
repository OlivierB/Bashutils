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

log system

# -*- coding: utf-8 -*-

from bashutils import logmsg


def test():
    print "COMPLETE PREDEFINED LOG"
    logmsg.log_success_msg("This is a success message")
    logmsg.log_failure_msg("This is a failure message")
    logmsg.log_error_msg("This is an error message")

    logmsg.log_msg_type("ALL Types handler", logmsg.LOG.OK)
    logmsg.log_msg_type("ALL Types handler", logmsg.LOG.FAIL)
    logmsg.log_msg_type("ALL Types handler", logmsg.LOG.ERROR)

    logmsg.log_begin_message("Two seconds action running...")
    logmsg.log_end_message(logmsg.LOG.OK)

    logmsg.log_begin_message("Test PRE message...")
    logmsg.log_end_msg_pre("PRE - ", logmsg.LOG.FAIL)

    logmsg.log_begin_message("Test POST message...")
    logmsg.log_end_msg_post("- /!\\ POST", logmsg.LOG.ERROR)

    logmsg.add_log_type("MLOG", "MY MEGA LOG", "red", "yellow")
    logmsg.log_msg_type("Test new log type", logmsg.LOG.MLOG)


if __name__ == "__main__":
    test()

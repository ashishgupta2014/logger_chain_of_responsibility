from source.logger.debug_log import DebugLog
from source.logger.error_log import ErrorLog
from source.logger.info_log import InfoLog


def main():
    info_log = InfoLog()
    debug_log = DebugLog()
    error_log = ErrorLog()
    info_log.set_next(debug_log).set_next(error_log)
    message = [('error', "Error message1"), ('debug', 'Debug message'), ('info', 'Info Message'), ('abcd', 'unknown')]
    for req, msg in message:
        info_log.handle(req, msg)


if __name__ == "__main__":
    main()

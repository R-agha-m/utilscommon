
try:
    from traceback import format_exc
    from signal import signal, SIGINT
    from os import environ
    from time import sleep

    STG_MODULE_ADDRESS = environ.setdefault("STG_MODULE_ADDRESS", "./stg.py")

    from stg import STG, report
    from workflow.workflow import Workflow

    workflow_obj = Workflow()
    workflow_obj.perform()

    if STG.SAFE_TERMINATION:
        if "windows" in STG.OS_TYPE:
            try:
                while True:
                    sleep(1)
            except KeyboardInterrupt:
                workflow_obj.stop_threads(signum=None, frame=None)

        else:
            try:
                signal(SIGINT, workflow_obj.stop_threads)
            except Exception:
                pass

except Exception:
    error_text = format_exc()

    try:
        report.critical(error_text)

    except Exception:
        error_text_4_report = format_exc()
        print(error_text)
        print("\n\n\n")
        print(error_text_4_report)

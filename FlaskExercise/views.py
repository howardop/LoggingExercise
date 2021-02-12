from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    app.logger.debug("main debug")
    if (log == 'info'):
        app.logger.info("main info")
    elif (log == 'warning'):  
        app.logger.warning("main warning")
    elif (log == 'error'):
        app.logger.error("main error")
    else:
        app.logger.critical("main critical")

    return render_template(
        'index.html',
        log=log
    )

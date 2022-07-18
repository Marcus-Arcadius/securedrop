# -*- coding: utf-8 -*-
from journalist_app import create_app
from sdconfig import config

app = create_app(config)


if __name__ == "__main__":  # pragma: no cover
    debug = getattr(config, "env", "prod") != "prod"
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(debug=debug, host="0.0.0.0", port=8081)  # nosec

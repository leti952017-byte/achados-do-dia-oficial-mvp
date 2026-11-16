import os

 from flask import Flask, jsonify, render_template


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)

    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key and not (config and config.get("SECRET_KEY")):
        raise RuntimeError("Defina SECRET_KEY no arquivo .env antes de iniciar a aplicação.")

    app.config.update(
        SECRET_KEY=secret_key,
        SUPABASE_URL=os.environ.get("SUPABASE_URL", ""),
        SUPABASE_ANON_KEY=os.environ.get("SUPABASE_ANON_KEY", ""),
        DEBUG=False,
    )

    if config:
        app.config.update(config)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app

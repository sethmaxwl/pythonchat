import logging
import os

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor

from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

if not app.debug:
    # Setup logging for app
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/chat.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)
    # app.logger.setLevel(logging.INFO)
    # app.logger.info('Chat server started')

    # Setup OpenTelemetry tracing for PubSub
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(CloudTraceSpanExporter())
    )



from app import routes

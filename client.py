from flask import Flask
from flask_bootstrap import Bootstrap
from google.cloud import pubsub_v1
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerPovider
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor

app = Flask(__name__)
Bootstrap(app)

TOPIC = 'chat-service'
SUBSCRIBER = 'chat-subscriber'

# Initialize tracer and setup trace exporter
def init_tracing():
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(CloudTraceSpanExporter())
    )

# Send a message
def publish_message(message):
    data = unicode(message, "utf-8")
    future = app.config["PUBLISHER"].publish(TOPIC, data)


if __name__ == '__main__':
    init_tracing()
    app.config["PUBLISHER"] = pubsub_v1.Publisher
    app.run(host='0.0.0.0', port=8080, debug=True)
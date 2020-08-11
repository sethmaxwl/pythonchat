from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from opentelemetry import trace
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor
from random import random

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(CloudTraceSpanExporter())
)

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path("sethmaxwl-playground", "test-subscription")

timeout = 60.0

def callback(message):
    if (random())

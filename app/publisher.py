from google.cloud import pubsub_v1

retry_settings = {
    "interfaces": {
        "google.pubsub.v1.Publisher": {
            "retry_codes": {
                "publish": [
                    "ABORTED",
                    "CANCELLED",
                    "DEADLINE_EXCEEDED",
                    "INTERNAL",
                    "RESOURCE_EXHAUSTED",
                    "UNAVAILABLE",
                    "UNKNOWN",
                ]
            },
            "retry_params": {
                "messaging": {
                    "initial_retry_delay_millis": 100,  # default: 100
                    "retry_delay_multiplier": 1.3,  # default: 1.3
                    "max_retry_delay_millis": 60000,  # default: 60000
                    "initial_rpc_timeout_millis": 5000,  # default: 25000
                    "rpc_timeout_multiplier": 1.0,  # default: 1.0
                    "max_rpc_timeout_millis": 600000,  # default: 30000
                    "total_timeout_millis": 600000,  # default: 600000
                }
            },
            "methods": {
                "Publish": {
                    "retry_codes_name": "publish",
                    "retry_params_name": "messaging",
                }
            },
        }
    }
}

publisher = pubsub_v1.PublisherClient(client_config=retry_settings)
topic_path = publisher.topic_path("sethmaxwl-playground", "chat-service")

def publish_message(msg):
    data = msg.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
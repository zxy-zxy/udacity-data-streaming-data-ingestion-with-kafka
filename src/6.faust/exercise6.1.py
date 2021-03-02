import faust

# See: https://faust.readthedocs.io/en/latest/userguide/application.html#application-parameters

BROKER_URL = "localhost:9092"
TOPIC_NAME = "com.udacity.streams.clickevents"

app = faust.App("my-faust-application", broker=BROKER_URL)

# See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description

topic = app.topic(TOPIC_NAME)

# See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-agent-define-a-new-stream-processor


@app.agent(topic)
async def clickevent(clickevents):
    async for event in clickevents:
        print(event)


if __name__ == "__main__":
    app.main()

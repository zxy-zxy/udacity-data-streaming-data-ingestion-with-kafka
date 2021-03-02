from dataclasses import dataclass

import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int


app = faust.App("exercise4", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)
popular_uris_topic = app.topic(
    "com.udacity.streams.clickevents.popular",
    key_type=str,
    value_type=ClickEvent,
)


@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for click_event in clickevents.filter(lambda x: x.number >= 100):
        await popular_uris_topic.send(key=click_event.uri, value=click_event)


if __name__ == "__main__":
    app.main()

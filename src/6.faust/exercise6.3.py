from dataclasses import asdict, dataclass
import json

import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int


@dataclass
class ClickEventSanitized(faust.Record):
    timestamp: str
    uri: str
    number: int


app = faust.App("exercise3", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)

sanitized_topic = app.topic("com.udacity.streams.clickevents.sanitized", key_type=str, value_type=ClickEventSanitized)


@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for clickevent in clickevents:
        sanitized_click_event = ClickEventSanitized(
            timestamp=clickevent.timestamp, uri=clickevent.uri, number=clickevent.number
        )
        await sanitized_topic.send(key=sanitized_click_event.uri, value=sanitized_click_event)


if __name__ == "__main__":
    app.main()

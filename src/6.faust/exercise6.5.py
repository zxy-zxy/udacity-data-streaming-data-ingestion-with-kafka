from dataclasses import dataclass
import random

import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int
    score: int = 0


def add_score(click_event):
    click_event.score = random.randint(0, 100)
    return click_event


app = faust.App("exercise5", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)
scored_topic = app.topic(
    "com.udacity.streams.clickevents.scored",
    key_type=str,
    value_type=ClickEvent,
)


@app.agent(clickevents_topic)
async def clickevent(clickevents: faust.Stream):
    clickevents.add_processor(add_score)
    async for ce in clickevents:
        await scored_topic.send(key=ce.uri, value=ce)


if __name__ == "__main__":
    app.main()

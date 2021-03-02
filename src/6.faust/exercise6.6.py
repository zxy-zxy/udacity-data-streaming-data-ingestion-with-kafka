from dataclasses import dataclass
import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int


app = faust.App("exercise6", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)
uri_summary_table = app.Table("uri_summary", default=int)


@app.agent(clickevents_topic)
async def clickevent(clickevents: faust.Stream):
    async for ce in clickevents.group_by(ClickEvent.uri):
        uri_summary_table[ce.uri] += ce.number
        current_uri_number = uri_summary_table[ce.uri]
        print(f"{ce.uri}: {current_uri_number}")


if __name__ == "__main__":
    app.main()

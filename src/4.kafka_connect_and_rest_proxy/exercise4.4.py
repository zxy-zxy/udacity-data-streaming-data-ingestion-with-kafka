import asyncio
from aiohttp import ClientSession

REST_PROXY_URL = "http://localhost:8082"


async def request_to_kafka_proxy(endpoint: str):
    url = f"{REST_PROXY_URL}/{endpoint}"
    async with ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.json()
            print(f"Response from {endpoint}: {content}")


async def main():
    await asyncio.gather(request_to_kafka_proxy("topics"), request_to_kafka_proxy("brokers"))


if __name__ == "__main__":
    asyncio.run(main())

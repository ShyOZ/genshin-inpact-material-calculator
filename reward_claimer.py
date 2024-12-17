import genshin
import asyncio
import keyboard


async def main():
    client = genshin.Client()
    tokens = genshin.utility.get_browser_cookies("firefox")
    client.set_cookies(tokens)

    await client.claim_daily_reward(game=genshin.Game.GENSHIN)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ...
    except Exception as e:
        print(e)
        keyboard.wait("enter")

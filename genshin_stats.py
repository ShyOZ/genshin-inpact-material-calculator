from io import StringIO
from attr import dataclass
import genshin
import asyncio
import pandas as pd
from tqdm import tqdm
from asyncio import sleep
from datetime import datetime, timezone, timedelta

from characters import rotation
from item_drops import *

"""traveler:
    Anemo:      9/9/7
    Geo:        1/1/1
    Electro:    1/1/1
    Dendro:     7/7/8
    Hydro:      6/7/9  
"""

BROWSER = "firefox"
PYRO = 1
ANEMO = 2
GEO = 3
DENDRO = 4
ELECTRO = 5
HYDRO = 6
CRYO = 7

@dataclass
class Consumable:
    id: int
    name: str
    amount: int


async def main(target_attack, target_skill, target_burst):
    client = genshin.Client()
    client.set_browser_cookies(BROWSER)

    now = datetime.now()
    server_now = datetime.now(tz=timezone(timedelta(hours=+1)))
    day = server_now.strftime("%A")
    day = "Sunday"  # uncomment this line to force all characters
    current_rotation = list(
        filter(
            lambda c: c.talents[0] < target_attack
            or c.talents[1] < target_skill
            or c.talents[2] < target_burst,
            rotation[day],
        )
    )
    current_rotation = list(map(lambda c: c.name, current_rotation))

    today_characters = [
        c
        for c in await client.get_calculator_characters(sync=True)
        if c.name in current_rotation
    ]

    df = pd.DataFrame(columns=["id", "name"])

    message_builder = StringIO("")
    remaining = len(today_characters)
    done = len(rotation[day]) - remaining

    for i, character in tqdm(enumerate(today_characters), total=len(today_characters)):
        costs = await (
            client.calculator()
            .set_character(character.id, current=character.level, target=90)
            .with_current_talents(
                attack=target_attack,
                skill=target_skill,
                burst=target_burst,
            )
        )

        consumables = costs.talents + costs.character
        
        accumulated_consumables = []
        
        for consumable in consumables:
            for accumulated_consumable in accumulated_consumables:
                if accumulated_consumable.name == consumable.name:
                    accumulated_consumable.amount += consumable.amount
                    break
            else:
                accumulated_consumables.append(Consumable(consumable.id, consumable.name, consumable.amount))

        # print(consumables)
    
        message_builder.write(f"\t{character.name}\n")
        df = pd.concat(
            [df, pd.DataFrame({c.name: c.amount for c in accumulated_consumables}, index=[i])]
        )
        df.loc[i, ["id", "name"]] = [consumable.id, consumable.name]

        await sleep(0.5)

    df.fillna(0, inplace=True)

    for boss, drops in weekly_drops.items():
        df[boss] = 0
        for drop in drops:
            if drop in df.columns:
                df[boss] += df[drop]
                df.drop(drop, axis=1, inplace=True)

    summary = df.iloc[:, 2:].sum(axis=0).astype(int).loc[lambda x: x > 0]

    summary.sort_index(inplace=True)

    with open("material_summary.txt", "w") as f:
        f.write(f"{now.strftime('%Y-%m-%d %H:%M')} (server time {server_now.strftime('%Y-%m-%d %H:%M')})\n")
        f.write(f"going for {target_attack}/{target_skill}/{target_burst}:\n")
        f.write(f"{done=}\n{remaining=}\n")
        f.write(f"{message_builder.getvalue()}\n")
        f.write(f"{summary.to_string()}\n")

async def temp():
    client = genshin.Client()
    client.set_browser_cookies(BROWSER)
    
    costs = await (
            client.calculator()
            .set_character(10000002, current=1, target=90)
            .with_current_talents(
                attack=6,
                skill=9,
                burst=9,
            )
        )
    
    consumables = costs.talents + costs.character
    
    df = pd.DataFrame(columns=["id", "name"])
    
    accumulated_consumables = []
        
    for consumable in consumables:
        for accumulated_consumable in accumulated_consumables:
            if accumulated_consumable.name == consumable.name:
                accumulated_consumable.amount += consumable.amount
                break
        else:
            accumulated_consumables.append(Consumable(consumable.id, consumable.name, consumable.amount))

    # print(consumables)

    df = pd.DataFrame({c.name: c.amount for c in accumulated_consumables}, index=[0])

    df.fillna(0, inplace=True)

    for boss, drops in weekly_drops.items():
        df[boss] = 0
        for drop in drops:
            if drop in df.columns:
                df[boss] += df[drop]
                df.drop(drop, axis=1, inplace=True)

    summary = df.iloc[:, 2:].sum(axis=0).astype(int).loc[lambda x: x > 0]

    summary.sort_index(inplace=True)
    
    print(summary)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(9, 9, 9))

import genshin
import asyncio
import pandas as pd
from tqdm import tqdm
from pprint import pprint
from asyncio import sleep
from datetime import datetime, timezone, timedelta

rotation = {
    "Monday": ["Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Tartaglia",  # Freedom
               "Keqing", "Ningguang", "Qiqi", "Shenhe", "Xiao", "Yelan",  # Prosperity
               "Kirara", "Sangonomiya Kokomi", "Shinkaoin Heizou", "Thoma", "Yoimiya",  # Transience
               "Candace", "Cyno", "Faruzan", "Tighnari",  # Admonition
               ],

    "Tuesday": ["Bennet", "Diluc", "Eula", "Jean", "Mona", "Noelle", "Razor",  # Resistance
                "Chongyun", "Ganyu", "Hu Tao", "Kaedehara Kazuha", "Xiangling", "YaoYao", "Yun Jin",  # Diligence
                "Itto", "Kamisato Ayaka", "Kamisato Ayato", "Kujou Sara", "Shinobu",  # Elegance
                "Alhaitham", "Dori", "Kaveh", "Layla", "Nahida",  # Ingenuity
                ],

    "Wednesday": ["Albedo", "Fischl", "Kaeya", "Lisa", "Mika", "Rosaria", "Venti",  # Ballad
                  "Baizhu", "Beidou", "Xingqiu", "Xinyan", "Yanfei", "Zhongli",  # Gold
                  "Gorou", "Raiden Shogun", "Sayu", "Yae Miko",  # Light
                  "Collei", "Dehya", "Nilou", "Wanderer",  # Praxis
                  ],
}

rotation["Thursday"] = rotation["Monday"]
rotation["Friday"] = rotation["Tuesday"]
rotation["Saturday"] = rotation["Wednesday"]
rotation["Sunday"] = rotation["Monday"] + rotation["Tuesday"] + rotation["Wednesday"]


def costs_to_dict(consumables):
    return pd.DataFrame({c.name: c.amount for c in consumables}, index=[0])


async def main():
    client = genshin.Client()
    tokens = genshin.utility.get_browser_cookies()
    client.set_cookies(tokens)

    character_info = [(c.id, c.name) for c in await client.get_calculator_characters(sync=True)]

    now = datetime.now(tz=timezone(timedelta(hours=-3)))
    day = now.strftime("%A")
    current_rotation = rotation[day]

    today_characters_info = [c for c in character_info if c[1] in current_rotation]

    df = pd.DataFrame(columns=['id', 'name'])

    for i, (c_id, c_name) in (pbar := tqdm(enumerate(today_characters_info), total=len(today_characters_info))):
        pbar.set_postfix_str(f'Processing {c_name}')

        costs = await (client.calculator()
                       .set_character(c_id, current=90, target=90)
                       .with_current_talents(target=9))

        consumables = costs.talents
        if not consumables:
            continue

        df = pd.concat([df, pd.DataFrame({c.name: c.amount for c in consumables}, index=[i])])
        df.loc[i, ['id', 'name']] = [c_id, c_name]

        await sleep(1)

    df.fillna(0, inplace=True)

    df.iloc[:, 2:] = df.iloc[:, 2:].astype(int)
    summary = df.iloc[:, 2:].sum(axis=0)

    summary.sort_index(inplace=True)

    pprint(summary)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    #
    # df = pd.DataFrame()
    # df = pd.concat([df, pd.DataFrame({'a': 1, 'b': 2}, index=[0])], ignore_index=True)
    # df = pd.concat([df, pd.DataFrame({'c': 3, 'd': 4}, index=[0])], ignore_index=True)
    #
    # print(df)

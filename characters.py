from attrs import define


@define(frozen=True)
class Character:
    name: str
    talents: tuple[int, int, int]


freedom_characters = [
    Character("Amber", (9, 9, 9)),
    Character("Barbara", (10, 9, 9)),
    Character("Sucrose", (9, 9, 9)),
    Character("Klee", (9, 9, 9)),
    Character("Diona", (9, 9, 9)),
    Character("Tartaglia", (9, 9, 9)),
    Character("Aloy", (9, 9, 9)),
]
resistance_characters = [
    Character("Bennett", (9, 9, 9)),
    Character("Diluc", (9, 9, 9)),
    Character("Jean", (9, 9, 9)),
    Character("Mona", (9, 9, 9)),
    Character("Noelle", (9, 9, 9)),
    Character("Razor", (9, 9, 9)),
    Character("Eula", (9, 9, 9)),
]
ballad_characters = [
    Character("Fischl", (9, 9, 9)),
    Character("Kaeya", (9, 9, 9)),
    Character("Lisa", (9, 9, 9)),
    Character("Venti", (9, 9, 9)),
    Character("Albedo", (9, 9, 9)),
    Character("Rosaria", (9, 9, 9)),
    Character("Mika", (9, 9, 9)),
]

prosperity_characters = [
    Character("Keqing", (9, 9, 9)),
    Character("Ningguang", (9, 9, 9)),
    Character("Qiqi", (9, 9, 9)),
    Character("Xiao", (9, 9, 9)),
    Character("Shenhe", (9, 9, 9)),
    Character("Yelan", (9, 9, 9)),
    Character("Gaming", (9, 9, 9)),
]
diligence_characters = [
    Character("Chongyun", (9, 9, 9)),
    Character("Xiangling", (9, 9, 9)),
    Character("Ganyu", (10, 9, 9)),
    Character("Hu Tao", (9, 9, 9)),
    Character("Kaedehara Kazuha", (9, 9, 9)),
    Character("Yun Jin", (9, 9, 9)),
    Character("Yaoyao", (9, 9, 9)),
]
gold_characters = [
    Character("Beidou", (9, 9, 9)),
    Character("Xingqiu", (9, 9, 9)),
    Character("Xinyan", (9, 9, 9)),
    Character("Zhongli", (9, 9, 9)),
    Character("Yanfei", (9, 9, 9)),
    Character("Baizhu", (9, 9, 9)),
    Character("Xianyun", (9, 9, 9)),
]

transience_characters = [
    Character("Yoimiya", (10, 9, 9)),
    Character("Sangonomiya Kokomi", (9, 9, 9)),
    Character("Thoma", (9, 9, 9)),
    Character("Shikanoin Heizou", (9, 9, 9)),
    Character("Kirara", (9, 9, 9)),
]
elegance_characters = [
    Character("Kamisato Ayaka", (9, 9, 9)),
    Character("Kujou Sara", (9, 9, 9)),
    Character("Arataki Itto", (9, 9, 9)),
    Character("Kamisato Ayato", (9, 9, 9)),
    Character("Kuki Shinobu", (9, 9, 9)),
]
light_characters = [
    Character("Sayu", (9, 9, 9)),
    Character("Raiden Shogun", (9, 9, 9)),
    Character("Gorou", (9, 9, 9)),
    Character("Yae Miko", (9, 9, 9)),
    Character("Chiori", (9, 9, 9)),
]

admonition_characters = [
    Character("Tighnari", (9, 9, 9)),
    Character("Candace", (9, 9, 9)),
    Character("Cyno", (9, 9, 9)),
    Character("Faruzan", (9, 9, 9)),
]
ingenuity_characters = [
    Character("Dori", (9, 9, 9)),
    Character("Nahida", (9, 9, 9)),
    Character("Layla", (9, 9, 9)),
    Character("Alhaitham", (9, 9, 9)),
    Character("Kaveh", (9, 9, 9)),
]
praxis_characters = [
    Character("Collei", (9, 9, 9)),
    Character("Nilou", (9, 9, 9)),
    Character("Wanderer", (9, 9, 9)),
    Character("Dehya", (9, 9, 9)),
    Character("Sethos", (9, 9, 9)),
]

equity_characters = [
    Character("Lyney", (9, 9, 9)),
    Character("Neuvillette", (9, 9, 9)),
    Character("Navia", (9, 9, 9)),
    # Character("Sigewinne", (1, 1, 1)),
]
justice_characters = [
    Character("Freminet", (9, 9, 9)),
    Character("Charlotte", (9, 9, 9)),
    Character("Furina", (9, 9, 9)),
    Character("Clorinde", (9, 9, 9)),
]
order_characters = [
    Character("Lynette", (9, 9, 9)),
    Character("Wriothesley", (9, 9, 9)),
    Character("Chevreuse", (9, 9, 9)),
    Character("Arlecchino", (9, 9, 9)),
    Character("Emilie", (9, 9, 9)),
]

contention_characters = [
    Character("Mualani", (9, 9, 9)),
]

conflict_characters = [
    Character("Kachina", (9, 9, 9)),
    Character("Chasca", (9, 9, 9)),
]

kindling_characters = [
    # Character("Kinich", (1, 1, 1)),
    Character("Xilonen", (9, 9, 9)),
    Character("Ororon", (9, 9, 9)),
]

characters_by_regions = {
    "Mondstadt": freedom_characters + resistance_characters + ballad_characters,
    "Liyue": prosperity_characters + diligence_characters + gold_characters,
    "Inazuma": transience_characters + elegance_characters + light_characters,
    "Sumeru": admonition_characters + ingenuity_characters + praxis_characters,
    "Fontaine": equity_characters + justice_characters + order_characters,
    "Natlan": contention_characters + conflict_characters + kindling_characters,
}

rotation = {
    "Monday": freedom_characters
    + prosperity_characters
    + transience_characters
    + admonition_characters
    + equity_characters
    + contention_characters,
    "Tuesday": resistance_characters
    + diligence_characters
    + elegance_characters
    + ingenuity_characters
    + justice_characters
    + kindling_characters,
    "Wednesday": ballad_characters
    + gold_characters
    + light_characters
    + praxis_characters
    + order_characters
    + conflict_characters,
}

rotation["Thursday"] = rotation["Monday"]
rotation["Friday"] = rotation["Tuesday"]
rotation["Saturday"] = rotation["Wednesday"]
rotation["Sunday"] = rotation["Monday"] + rotation["Tuesday"] + rotation["Wednesday"]

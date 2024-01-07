class ability:
    def __init__(self):
        self.range = 0
        self.targetranges = 0
        self.effectrad = 0
        self.colrad = 0


class champ:
    def __init__(self, name="", aarange=0, q=None, w=None, e=None, r=None):
        self.name = name
        self.aarange = aarange
        self.q = ability()
        self.w = ability()
        self.e = ability()
        self.r = ability()


def sanitize(name):
    # sanitize input
    name = name.title()
    # stupid special cases
    # asol. lee. mf. nunu? renata. tahm. tf. EVERY ' CHAMP BRO
    match name:
        case "AurelionSol":
            name = "Aurelion_Sol"
        case "Asol":
            name = "Aurelion_Sol"
        case "Belveth":
            name = "Bel'Veth"
        case "DrMundo":
            name = "Mundo"
        case "JarvanIV":
            name = "Jarvan_IV"
        case "J4":
            name = "Jarvan_IV"
        case "KogMaw":
            name = "Kog'Maw"  # wiki still works with "Kogmaw"
        case "Kog":
            name = "Kog'Maw"
        case "KSante":
            name = "K'Sante"
        case "Ksante":
            name = "K'Sante"
        case "LeeSin":
            name = "Lee_Sin"
        case "Lee":
            name = "Lee_Sin"
        case "MasterYi":
            name = "Master_Yi"
        case "Yi":
            name = "Master_Yi"
        case "MissFortune":
            name = "Miss_Fortune"
        case "Mf":
            name = "Miss_Fortune"
        case "MonkeyKing":
            name = "Wukong"
        case "Reksai":
            name = "Rek'Sai"
        case "Renata":
            name = "Renata_Glasc"  # wiki still works with "Renata"
        case "TahmKench":
            name = "Tahm_Kench"
        case "Tahm":
            name = "Tahm_Kench"
        case "TwistedFate":
            name = "Twisted_Fate"
        case "Tf":
            name = "Twisted_Fate"
        case "Velkoz":
            name = "Vel'koz"  # wiki still works with "Velkoz"
        case "XinZhao":
            name = "Xin_Zhao"
        case "Xin":
            name = "Xin_Zhao"
        case _:
            return name
            
        
    return name


def callWiki(name):
    from bs4 import BeautifulSoup
    import requests

    name = sanitize(name)

    # create new champ object
    champion = champ()
    champion.name = name

    url = f"https://leagueoflegends.fandom.com/wiki/{name}/LoL"
    # Make a request
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="utf-8")

    # for aa
    try:
        champion.aarange = soup.find(id=f"AttackRange_{name}").text
    except:
        print("champ does not exist")
        return -1

    # for q ability
    qAbilitySection = soup.find("div", attrs={"class": "skill skill_q"})

    # ranges
    elements = qAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.q.range = test[2]
    # target ranges
    elements = qAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "target range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.q.targetranges = test[2]

    # effect radius
    elements = qAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "effect radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.q.effectrad = test[2]

    # collision radius
    elements = qAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "collision radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.q.colrad = test[2]

    
    # for w ability
    wAbilitySection = soup.find("div", attrs={"class": "skill skill_w"})

    # ranges
    elements = wAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.w.range = test[2]
    # target ranges
    elements = wAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "target range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.w.targetranges = test[2]

    # effect radius
    elements = wAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "effect radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.w.effectrad = test[2]

    # collision radius
    elements = wAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "collision radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.w.colrad = test[2]



    
    # for e ability
    eAbilitySection = soup.find("div", attrs={"class": "skill skill_e"})
    # ranges
    elements = eAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.e.range = test[2]
    # target ranges
    elements = eAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "target range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.e.targetranges = test[2]

    # effect radius
    elements = eAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "effect radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.e.effectrad = test[2]

    # collision radius
    elements = eAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "collision radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.e.colrad = test[2]

    

    # for r ability
    rAbilitySection = soup.find("div", attrs={"class": "skill skill_r"})
    # ranges
    elements = rAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.r.range = test[2]
    # target ranges
    elements = rAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "target range"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.r.targetranges = test[2]

    # effect radius
    elements = rAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "effect radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.r.effectrad = test[2]

    # collision radius
    elements = rAbilitySection.find_all(
        class_="pi-item pi-data pi-item-spacing pi-border-color",
        attrs={"data-source": "collision radius"},
    )
    for element in elements:
        test = element.text.splitlines()
        champion.r.colrad = test[2]

    return champion


def ingame(name):
    import os
    from riotwatcher import LolWatcher, ApiError

    key = os.getenv(apikey)
    # API KEY DO NOT PUBLISH API KEY DO NOT PUBLISH API KEY DO NOT PUBLISH
    lol_watcher = LolWatcher(key)

    my_region = "na1"
    my_name = name
    # id = encrypted summoner id
    # accountId = encrypted account id
    # puuid = encrypted puuid
    try:
        me = lol_watcher.summoner.by_name(my_region, name)
    except ApiError as err:
        if err.response.status_code == 404:
            # print('cannot find person with that name')
            return -2
        else:
            raise

    # First we get the latest version of the game from data dragon
    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions["n"]["champion"]
    # print(champions_version)
    test = lol_watcher.data_dragon.champions(champions_version, True)
    keys = test["keys"]

    # try to find game of 'me' currently ingame
    try:
        lol_watcher.spectator.by_summoner(my_region, me["id"])
    except ApiError as err:
        if err.response.status_code == 404:
            # print("not in game")
            return -1

    # since program didn't return, continue logic
    curr_game = lol_watcher.spectator.by_summoner(my_region, me["id"])
    playerlist = curr_game["participants"]
    # print out all champions
    # print("playlist:")
    # print(playerlist)
    champlist = []
    for i in playerlist:
        # typecast to a string
        champlist.append(keys[str(i.get("championId"))])

    champObjectList = []
    for x in champlist:
        champObjectList.append(callWiki(x))

    return champObjectList

from json import load, dump
from datetime import datetime
from BuildArchives import new_archive
import random
import ntchat
from os import getcwd
from os.path import join
from time import sleep
wechat = ntchat.WeChat()
def slip(from_wxid):
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    if origin[from_wxid]["fortune"] == 0:
        return True


def fortune(from_wxid):
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)

    if datetime.now().strftime("%Y%m%d") != origin["date"]:
        origin["date"] = datetime.now().strftime("%Y%m%d")
        for key in origin.keys():
            if key in ["date", "last_setu"]:
                continue
            origin[key]["fortune"] = 0

    if from_wxid not in origin.keys():
        new_archive(from_wxid)
        with open("info.json", mode="r", encoding="utf-8") as f:
            origin = load(f)
    if origin[from_wxid]["fortune"]==1:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是大凶捏\n但无论如何，「命]与「运」都应该自己掌握、自己开拓吧。"
    if origin[from_wxid]["fortune"]==2:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是凶捏\n可以结在「御签挂」上，以求转运哦。"
    if origin[from_wxid]["fortune"]==3:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是末吉\n文字位招租"
    if origin[from_wxid]["fortune"]==4:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是中吉\n文字位招租"
    if origin[from_wxid]["fortune"]==5:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是吉\n文字位招租"
    if origin[from_wxid]["fortune"]==6:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经抽过了，是大吉\n文字位招租"



    point = random.randint(1, 112)
    if point <= 2:
        origin[from_wxid]["fortune"] = 1
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——大凶——\n内心空落落的一天。可能会陷入深深的无力感之中。\n很多事情都无法理清头绪，过于钻牛角尖则易生病。\n虽然一切皆陷于低潮谷底中，但也不必因此而气馁。\n若能撑过一时困境，他日必另有一番作为。\n\n今天的幸运物是：弯弯曲曲的「蜥蜴尾巴」\n蜥蜴遇到潜在的危险时，大多数会断尾求生。\n若是遇到无法整理的情绪，那么该断则断吧。"
    elif point <= 4:
        origin[from_wxid]["fortune"] = 2
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——凶——\n珍惜的东西可能会遗失，需要小心。\n如果身体有不适，一定要注意休息。\n在做出决定之前，一定要再三思考。\n\n今天的幸运物是：冰凉冰凉的「冰雾花」。\n冰雾花散发着「生人勿进」的寒气。\n但有时冰冷的气质，也能让人的心情与头脑冷静下来。\n据此采取正确的判断，明智地行动"
    elif point <= 6:
        origin[from_wxid]["fortune"] = 2
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——凶——\n隐约感觉会下雨的一天。可能会遇到不顺心的事情。\n应该的褒奖迟迟没有到来，服务生也可能会上错菜。\n明明没什么大不了的事，却总感觉有些心烦的日子。\n——难免有这样的日子——\n\n今天的幸运物是：随波摇曳的「海草」。\n海草是相当温柔而坚强的植物，\n即使在苦涩的海水中，也不愿改变自己。\n即使在逆境中，也不要放弃温柔的心灵。"
    elif point <= 16:
        origin[from_wxid]["fortune"] = 3
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——末吉——\n云遮月半边，雾起更迷离。\n抬头即是浮云遮月，低头则是浓雾漫漫。\n虽然一时前路迷惘，但也会有一切明了的时刻。\n现下不如趁此机会磨炼自我，等待拨云见皎月。\n\n今天的幸运物是：暗中发亮的「发光髓」。\n发光髓努力地发出微弱的光芒。\n虽然比不过其他光源，但看清前路也够用了。"
    elif point <= 26:
        origin[from_wxid]["fortune"] = 3
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——末吉——\n空中的云层偏低，并且仍有堆积之势，\n不知何时雷雨会骤然从头顶倾盆而下。\n但是等雷雨过后，还会有彩虹在等着。\n宜循于旧，守于静，若妄为则难成之。\n\n今天的幸运物是：树上掉落的「松果」。\n并不是所有的松果都能长成高大的松树，\n成长需要适宜的环境，更需要一点运气。\n所以不用给自己过多压力，耐心等待彩虹吧。"
    elif point <= 36:
        origin[from_wxid]["fortune"] = 3
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——末吉——\n平稳安详的一天。没有什么令人难过的事情会发生。\n适合和久未联系的朋友聊聊过去的事情，一同欢笑。\n吃东西的时候会尝到很久以前体验过的过去的味道。\n——要珍惜身边的人与事——\n\n今天的幸运物是：酥酥麻麻的「电气水晶」。\n电气水晶蕴含着无限的能量。\n如果能够好好导引这股能量，说不定就能成就什么事业。"
    elif point <= 46:
        origin[from_wxid]["fortune"] = 3
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——末吉——\n气压稍微有点低，是会令人想到遥远的过去的日子。\n早已过往的年轻岁月，与再没联系过的故友的回忆，\n会让人感到一丝平淡的怀念，又稍微有一点点感伤。\n——偶尔怀念过去也很好。放松心情面对未来吧——\n\n今天的幸运物是：清新怡人的「薄荷」。\n只要有草木生长的空间，就一定有薄荷。\n这么看来，薄荷是世界上最强韧的生灵。\n据说连蒙德的雪山上也长着薄荷呢。"
    elif point <= 66:
        origin[from_wxid]["fortune"] = 4
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——中吉——\n天上有云飘过的日子，天气令人十分舒畅。\n工作非常顺利，连午睡时也会想到好点子。\n突然发现，与老朋友还有其他的共同话题…\n——每一天，每一天都要积极开朗地度过——\n\n今天的幸运物是：色泽艳丽的「堇瓜」。\n人们常说表里如一是美德，\n但堇瓜明艳的外貌下隐藏着的是谦卑而甘甜的内在。"
    elif point <= 86:
        origin[from_wxid]["fortune"] = 4
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——中吉——\n十年磨一剑，今朝示霜刃。\n恶运已销，身临否极泰来之时。\n苦练多年未能一显身手的才能，\n现今有了大展身手的极好机会。\n若是遇到阻碍之事，亦不必迷惘，\n大胆地拔剑，痛快地战斗一番吧。\n\n今天的幸运物是：生长多年的「海灵芝」。\n弱小的海灵芝虫经历多年的风风雨雨，才能结成海灵芝。\n为目标而努力前行的人们，最终也必将拥有胜利的果实。"
    elif point <= 72:
        origin[from_wxid]["fortune"] = 5
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——吉——\n明明没有什么特别的事情，却感到心情轻快的日子。\n在没注意过的角落可以找到本以为丢失已久的东西。\n食物比平时更加鲜美，路上的风景也令人眼前一亮。\n——这个世界上充满了新奇的美好事物——\n\n今天的幸运物是：散发暖意的「鸟蛋」。\n鸟蛋孕育着无限的可能性，是未来之种。\n反过来，这个世界对鸟蛋中的生命而言，\n也充满了令其兴奋的未知事物吧。\n要温柔对待鸟蛋喔。"
    elif point <= 78:
        origin[from_wxid]["fortune"] = 5
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——吉——\n枯木逢春，正当万物复苏之时。\n陷入困境时，能得到解决办法。\n举棋不定时，会有贵人来相助。\n可以整顿一番心情，清理一番家装，\n说不定能发现意外之财。\n\n今天的幸运物是：节节高升的「竹笋」。\n竹笋拥有着无限的潜力，\n没有人知道一颗竹笋，到底能长成多高的竹子。\n看着竹笋，会让人不由自主期待起未来吧。"
    elif point <= 84:
        origin[from_wxid]["fortune"] = 5
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——吉——\n一如既往的一天。身体和心灵都适应了的日常。\n出现了能替代弄丢的东西的物品，令人很舒心。\n和常常遇见的人关系会变好，可能会成为朋友。\n——无论是多寻常的日子，都能成为宝贵的回忆——\n\n今天的幸运物是：闪闪发亮的「晶核」。\n晶蝶是凝聚天地间的元素，而长成的细小生物。\n而元素是这个世界许以天地当中的人们的祝福。"
    elif point <= 91:
        origin[from_wxid]["fortune"] = 6
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——大吉——\n会起风的日子，无论干什么都会很顺利的一天。\n周围的人心情也非常愉快，绝对不会发生冲突，\n还可以吃到一直想吃，但没机会吃的美味佳肴。\n无论是工作，还是旅行，都一定会十分顺利吧。\n那么，应当在这样的好时辰里，一鼓作气前进…\n\n今天的幸运物是：茁壮成长的「鸣草」。\n许多人或许不知道，鸣草是能预报雷暴的植物。\n向往着雷神大人的青睐，只在稻妻列岛上生长。\n摘下鸣草时酥酥麻麻的触感，据说和幸福的滋味很像。"
    elif point <= 98:
        origin[from_wxid]["fortune"] = 6
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——大吉——\n宝剑出匣来，无往不利。出匣之光，亦能照亮他人。\n今日能一箭射中空中的猎物，能一击命中守卫要害。\n若没有目标，不妨四处转转，说不定会有意外之喜。\n同时，也不要忘记和倒霉的同伴分享一下好运气哦。\n\n今天的幸运物是：难得一见的「马尾」。\n马尾随大片荻草生长，但却更为挺拔。\n与傲然挺立于此世的你一定很是相配。"
    elif point <= 105:
        origin[from_wxid]["fortune"] = 6
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——大吉——\n失而复得的一天。\n原本以为石沉大海的事情有了好的回应，\n原本分道扬镳的朋友或许可以再度和好，\n不经意间想起了原本已经忘记了的事情。\n世界上没有什么是永远无法挽回的，\n今天就是能够挽回失去事物的日子。\n\n今天的幸运物是：活蹦乱跳的「鬼兜虫」。\n鬼兜虫是爱好和平、不愿意争斗的小生物。\n这份追求平和的心一定能为你带来幸福吧。"
    elif point <= 112:
        origin[from_wxid]["fortune"] = 6
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} \n你今天的运势是\n——大吉——\n浮云散尽月当空，逢此签者皆为上吉。\n明镜在心清如许，所求之事心想则成。\n合适顺心而为的一天，不管是想做的事情，\n还是想见的人，现在是行动起来的好时机。\n\n今天的幸运物是：不断发热的「烈焰花花蕊」。\n烈焰花的炙热来自于火辣辣的花心。\n万事顺利是因为心中自有一条明路。"



if __name__ == '__main__':
    print(fortune("wxid_pdb55y5c8l5n12"))
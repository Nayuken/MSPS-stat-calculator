""" Reference: https://ayumilovemaple.wordpress.com/2009/09/06/maplestory-formula-compilation/"""

class Weaponformula:
    def __init__(self,str,dex,int,luk,wp_attk,wp_type):
        self.str = str
        self.dex = dex
        self.int = int
        self.luk = luk
        self.wp_attk = wp_attk
        self.wp_type = wp_type
    def weapon_stats(self):
        primary = 0
        secondary = 0
        onehanded_sword = [self.str * 4.0, self.dex]

        # Includes: Axe / BW / Wand / Staff
        onehanded_alt= [self.str * 4.4, self.dex]

        twohanded_sword = [self.str * 4.6, self.dex]

        # Includes: Axe/Bw
        twohanded_alt = [self.str * 4.8, self.dex]

        spear = [self.str * 5.0, self.dex]

        polearm = [self.str * 5.0, self.dex]

        #Includes dagger and claw
        thief = [self.luk * 3.6, self.str + self.dex]

        bow = [self.dex * 3.4, self.str]

        xbow = [self.dex * 3.6, self.str]

        knuckle = [self.str * 4.8, self.dex]

        gun = [self.dex * 3.6, self.str]

        #TODO: make it so all case sense can be read from list provided
        weapons_dict = {"1h sword":onehanded_sword, "1h axe": onehanded_alt, "1h bw": onehanded_alt, "2h sword":twohanded_sword, "2h axe": twohanded_alt,"2h bw": twohanded_alt,"spear":spear,"polearm":polearm,"dagger":thief,"claw":thief,"bow":bow,"xbox":xbow,"knuckle":knuckle,"gun":gun}
        input_list = ["1h sword", "1h axe", "1h bw", "2h sword", "2h axe", "2h bw", "spear", "polearm", "dagger", "claw","bow","xbow","knuckle","gun"]
        input_answered = True
        while input_answered:
            weapon_input = self.wp_type
            # weapon_input = input("Please enter a weapon type from the list: "
            #                      "\n\t 1h sword"
            #                      "\n\t 1h axe"
            #                      "\n\t 1h bw"
            #                      "\n\t 2h sword"
            #                      "\n\t 2h axe"
            #                      "\n\t 2h bw"
            #                      "\n\t spear"
            #                      "\n\t polearm"
            #                      "\n\t dagger"
            #                      "\n\t claw"
            #                      "\n\t bow"
            #                      "\n\t xbow"
            #                      "\n\t knuckle"
            #                      "\n\t gun "
            #                      "\n\t: ")
            if weapon_input not in input_list:
                print("please only enter only enter a weapon type from the list provided\n")
            else:
                input_answered = False
        for key,value in weapons_dict.items():
            if key == weapon_input:
                primary = value[0]
                secondary = value[1]
        return primary, secondary

    def weapon_calc(self):
        primary_stat, secondary_stat = Weaponformula.weapon_stats(self)

        """General Formula"""
        # MAX = (Primary Stat + Secondary Stat) * Weapon
        # Attack / 100
        # MIN = (Primary Stat * 0.9 * Skill Mastery + Secondary Stat) * Weapon
        # Attack / 100

        mastery = 0.6
        Max_range = (primary_stat + secondary_stat) * self.wp_attk / 100
        Min_range = (primary_stat * 0.9 * mastery + secondary_stat) * self.wp_attk / 100
        result = f"With the values provided your range is: {int(Min_range)} ~ {int(Max_range)}"
        result_alt = "With the values provided your range is " +str(int(Min_range))+"~" +str(int(Max_range))
        #print(f"With the values provided your range is: {int(Min_range)} ~ {int(Max_range)}")
        return result_alt

# def main():
#     strength = input("please provide your STR stat ")
#     stat_check = True
#     while stat_check:
#         try:
#             while True:
#                 if int(strength) < 0:
#                     strength = input("please provide only positive number values for your STR stat ")
#                 else:
#                     break
#             int_checker = int(strength)
#         except ValueError:
#             strength = input("please provide only number values for your STR stat ")
#         else:
#             stat_check = False
#
#     dex = input("please provide your DEX stat ")
#     stat_check = True
#     while stat_check:
#         try:
#             while True:
#                 if int(dex) < 0:
#                     dex = input("please provide only positive number values for your DEX stat ")
#                 else:
#                     break
#             int_checker = int(dex)
#         except ValueError:
#             dex = input("please provide only number values for your DEX stat ")
#         else:
#             stat_check = False
#
#     intelligence = input("please provide your INT stat ")
#     stat_check = True
#     while stat_check:
#         try:
#             while True:
#                 if int(intelligence) < 0:
#                     intelligence = input("please provide only positive number values for your INT stat ")
#                 else:
#                     break
#             int_checker = int(intelligence)
#         except ValueError:
#             intelligence = input("please provide only number values for your INT stat ")
#         else:
#             stat_check = False
#
#     luk = input("please provide your LUK stat ")
#     stat_check = True
#     while stat_check:
#         try:
#             while True:
#                 if int(luk) < 0:
#                     luk = input("please provide only positive number values for your LUK stat ")
#                 else:
#                     break
#             int_checker = int(luk)
#         except ValueError:
#             luk = input("please provide only number values for your LUK stat ")
#         else:
#             stat_check = False
#
#     weapon_attack = input("please calculate your weapon attack on all gear and provide the total ")
#     stat_check = True
#     while stat_check:
#         try:
#             while True:
#                 if int(weapon_attack) < 0:
#                     weapon_attack = input("please provide only positive number values for your LUK stat ")
#                 else:
#                     break
#             int_checker = int(weapon_attack)
#         except ValueError:
#             weapon_attack = input("please provide only number values for your LUK stat ")
#         else:
#             stat_check = False
#
#     player = Weaponformula(int(strength),int(dex),int(intelligence),int(luk),int(weapon_attack))
#     player.weapon_calc()
#     redo = input("Would you like to use the range calculator again? (yes or no)")
#     yes = "yes"
#     no = "no"
#     while True:
#         if redo.upper() == no.upper():
#             quit()
#         elif redo.upper() == yes.upper():
#             main()
#         else:
#             redo = input("Only answer with yes or no: ")

# if __name__ == "__main__":
#     main()
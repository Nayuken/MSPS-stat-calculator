""" References:
https://ayumilovemaple.wordpress.com/2009/09/06/maplestory-formula-compilation/
https://forum.maplelegends.com/index.php?threads/nises-formula-compilation.36234/
"""

class Weaponformula:
    def __init__(self,str,dex,int,luk,wp_attk,wp_type,throwable, bof):
        self.str = str
        self.dex = dex
        self.int = int
        self.luk = luk
        self.wp_attk = wp_attk
        self.wp_type = wp_type
        self.throwable = throwable
        self.bof = bof
    def throwable_stats(self):
        throwable_item = 0
        """Stars"""
        cilbis = 29
        cracker_shooter = 31
        mtk = 33
        itk = 35
        fts = 37
        wgt = 39

        """Bullets"""
        shiny_bullet = 18
        eternal_bullet = 20
        ap_bullet = 22
        giant_bullet = 24
        plaser_bullet = 26
        rlaser_bullet = 28

        """Arrows"""
        red_arrow = 3
        diamond_arrow = 4
        quality_arrow = 5
        strong_arrow = 7
        sharp_arrow = 9
        titanium_arrow = 11

        throwable_dict = {"Melee Class": throwable_item, "Crystal Ilbis": cilbis, "Cracker Shooter": cracker_shooter, "Magic Throwing Knife": mtk, "Infinite Throwing Knife": itk, "Flame Throwing Star": fts, "White Gold Throwing Star": wgt,
                          "Shiny Bullet":shiny_bullet,"Eternal Bullet":eternal_bullet, "Armor Piercing Bullet":ap_bullet, "Giant Bullet":giant_bullet, "Purple laser Bullet":plaser_bullet, "Red laser Bullet":rlaser_bullet,
                          "Red Arrow":red_arrow,"Diamond Arrow":diamond_arrow,"Quality Arrow":quality_arrow, "Strong Arrow":strong_arrow, "Sharp Arrow":sharp_arrow, "Titanium Arrow": titanium_arrow}
        for key,value in throwable_dict.items():
            if key == self.throwable:
                throwable_item = value
        return throwable_item

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

        weapons_dict = {"1h sword":onehanded_sword, "1h axe": onehanded_alt, "1h bw": onehanded_alt, "2h sword":twohanded_sword, "2h axe": twohanded_alt,"2h bw": twohanded_alt,"spear":spear,"polearm":polearm,"dagger":thief,"claw":thief,"bow":bow,"xbox":xbow,"knuckle":knuckle,"gun":gun}

        for key,value in weapons_dict.items():
            if key == self.wp_type:
                primary = value[0]
                secondary = value[1]
        return primary, secondary

    def weapon_calc(self):
        primary_stat, secondary_stat = Weaponformula.weapon_stats(self)
        attack_stat = self.wp_attk + Weaponformula.throwable_stats(self) +self.bof

        """General Formula"""
        # MAX = (Primary Stat + Secondary Stat) * Weapon
        # Attack / 100
        # MIN = (Primary Stat * 0.9 * Skill Mastery + Secondary Stat) * Weapon
        # Attack / 100
        mastery = 0.6
        if self.wp_type == "bow" or self.wp_type == "xbow":
            mastery = 0.9
            self.wp_attk += 10
        Max_range = (primary_stat + secondary_stat) * attack_stat / 100
        Min_range = (primary_stat * 0.9 * mastery + secondary_stat) * attack_stat / 100
        result = "With the values provided your range is " +str(int(Min_range))+"~" +str(int(Max_range))
        return result

    #TODO work on implementing base magic formula
    def magic_calc(self):
        pass
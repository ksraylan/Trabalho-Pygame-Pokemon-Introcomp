class Moves:
    def __init__(self):
        pass

    # geração 3 (talvez não precise):
    
    @property
    def aerial_ace(self):
        return 0
    @property
    def air_cutter(self):
        return 1
    @property
    def arm_thrust(self):
        return 2
    @property
    def aromatherapy(self):
        return 3
    @property
    def assist(self):
        return 4
    @property
    def astonish(self):
        return 5
    @property
    def blast_burn(self):
        return 6
    @property
    def blaze_kick(self):
        return 7
    @property
    def block(self):
        return 8
    @property
    def bounce(self):
        return 9
    @property
    def brick_break(self):
        return 10
    @property
    def bulk_up(self):
        return 11
    @property
    def bullet_seed(self):
        return 12
    @property
    def calm_mind(self):
        return 13
    @property
    def camouflage(self):
        return 14
    @property
    def charge(self):
        return 15
    @property
    def cosmic_power(self):
        return 16
    @property
    def covet(self):
        return 17
    @property
    def crush_claw(self):
        return 18
    @property
    def dive(self):
        return 19
    @property
    def doom_desire(self):
        return 20
    @property
    def dragon_claw(self):
        return 21
    @property
    def dragon_dance(self):
        return 22
    @property
    def endeavor(self):
        return 23
    @property
    def eruption(self):
        return 24
    @property
    def extrasensory(self):
        return 25
    @property
    def facade(self):
        return 26
    @property
    def fake_out(self):
        return 27
    @property
    def fake_tears(self):
        return 28
    @property
    def feather_dance(self):
        return 29
    @property
    def flatter(self):
        return 30
    @property
    def focus_punch(self):
        return 31
    @property
    def follow_me(self):
        return 32
    @property
    def frenzy_plant(self):
        return 33
    @property
    def grass_whistle(self):
        return 34
    @property
    def grudge(self):
        return 35
    @property
    def hail(self):
        return 36
    @property
    def heat_wave(self):
        return 37
    @property
    def helping_hand(self):
        return 38
    @property
    def howl(self):
        return 39
    @property
    def hydro_cannon(self):
        return 40
    @property
    def hyper_voice(self):
        return 41
    @property
    def ice_ball(self):
        return 42
    @property
    def icicle_spear(self):
        return 43
    @property
    def imprison(self):
        return 44
    @property
    def ingrain(self):
        return 45
    @property
    def iron_defense(self):
        return 46
    @property
    def knock_off(self):
        return 47
    @property
    def leaf_blade(self):
        return 48
    @property
    def luster_purge(self):
        return 49
    @property
    def magic_coat(self):
        return 50
    @property
    def megical_leaf(self):
        return 51
    @property
    def memento(self):
        return 52
    @property
    def metal_sound(self):
        return 53
    @property
    def meteor_mash(self):
        return 54
    @property
    def mist_ball(self):
        return 55
    @property
    def mud_shot(self):
        return 56
    @property
    def mud_sport(self):
        return 57
    @property
    def muddy_water(self):
        return 58
    @property
    def nature_power(self):
        return 59
    @property
    def needle_arm(self):
        return 60
    @property
    def odor_sleuth(self):
        return 61
    @property
    def overheat(self):
        return 62
    @property
    def poison_fang(self):
        return 63
    @property
    def poison_tail(self):
        return 64
    @property
    def psycho_boost(self):
        return 65
    @property
    def recycle(self):
        return 66
    @property
    def reflesh(self):
        return 67
    @property
    def revenge(self):
        return 68
    @property
    def rock_blast(self):
        return [69, "Rock Blast"]
    @property
    def rock_tomb(self):
        return 70
    @property
    def role_play(self):
        return 71
    @property
    def sand_tomb(self):
        return 72
    @property
    def secret_power(self):
        return 73
    @property
    def shadow_punch(self):
        return [74, "Shadow Punch"]
    @property
    def sheer_cold(self):
        return 75
    @property
    def shock_wave(self):
        return 76
    @property
    def signal_beam(self):
        return 77
    @property
    def silver_wind(self):
        return 78
    @property
    def skill_swap(self):
        return 79
    @property
    def sky_uppercut(self):
        return 80
    @property
    def slack_off(self):
        return 81
    @property
    def smelling_salts(self):
        return 82
    @property
    def snatch(self):
        return 83
    @property
    def spit_up(self):
        return 84
    @property
    def stockpile(self):
        return 85
    @property
    def superpower(self):
        return 86
    @property
    def swallow(self):
        return 87
    @property
    def tail_grow(self):
        return 88
    @property
    def taunt(self):
        return 89
    @property
    def teeter_dance(self):
        return 90
    @property
    def tickle(self):
        return 91
    @property
    def torment(self):
        return 92
    @property
    def trick(self):
        return 93
    @property
    def uproar(self):
        return 94
    @property
    def volt_tackle(self):
        return 95
    @property
    def water_pulse(self):
        return 96
    @property
    def water_sport(self):
        return 97
    @property
    def water_spout(self):
        return 98
    @property
    def wheather_ball(self):
        return 99
    @property
    def will_o_wisp(self):
        return 100
    @property
    def wish(self):
        return 101
    @property
    def yawm(self):
        return 102
    


    # geração 1. exemplo: return [id, nome, prioridade, força, chance_de_acertar, quantidade_de_pp] 
    @property
    def tackle(self):
        return [-1, "Tackle", 0, 35, 100, 35]
    @property
    def growl(self):
        return [-2, "Growl", 0, -6, 100, 40]
    @property
    def leech_seed(self):
        return [-3, "Leech Seed", 0, 0, 90, 10]
    @property
    def vine_whip(self):
        return [-4, "Vine Whip", 0, 45, 100, 25]
    @property
    def poison_powder(self):
        return [-5, "Poison Powder", 0, 0, 75, 35]
    @property
    def sleep_powder(self):
        return [-6, "Sleep Powder", 0, 0, 75, 15]
    @property
    def razor_leaf(self):
        return [-7, "Razor Leaf", 0, 55, 95, 25]
    @property
    def sweet_scent(self):
        return [-8, "Sweet Scent", 0, -6, 100, 20]
    @property
    def growth(self):
        return [-9, "Growth", 0, 6, 100, 20]
    @property
    def synthesis(self):
        return [-10, "Synthesis", 3, 50, 100, 5]
    @property
    def solar_beam(self):
        return [-11, "Solar Beam", 0, 120, 100, 10]
    @property
    def thunder_shock(self):
        return [-12, "Thunder Shock", 0, 40, 100, 30]
    @property
    def tail_whip(self):
        return [-13, "Tail Whip", 0, -6, 100, 30]
    @property
    def quick_attack(self):
        return [-14, "Quick Attack", 1, 40, 100, 30]
    @property
    def double_team(self):
        return [-15, "Double Team", 0, 6, 100, 15]
    @property
    def slam(self):
        return [-16, "Slam", 0, 80, 75, 20]
    @property
    def thunderbolt(self):
        return [-17, "Thunderbolt", 0, 95, 100, 15]
    @property
    def agility(self):
        return [-18, "Agility", 0, 6, 100, 30]
    @property
    def thunder(self):
        return [-19, "Thunder", 0, 120, 70, 10]
    @property
    def light_screen(self):
        return [-20, "Light Screen", 0, 0, 100, 30]
    @property
    def thunder_wave(self):
        return [-21, "Thunder Wave", 0, 0, 100, 20]
    @property
    def scratch(self):
        return [-22, "Scratch", 0, 40, 100, 35]
    @property
    def ember(self):
        return [-23, "Ember", 0, 40, 100, 25]
    @property
    def smokescreen(self):
        return [-24, "Smokescreen", 0, -6, 100, 20]
    @property
    def rage(self):
        return [-25, "Rage", 0, 20, 100, 20]
    @property
    def scary_face(self):
        return [-26, "Scary Face", 0, -6, 100, 10]
    @property
    def flamethrower(self):
        return [-27, "Flamethrower", 0, 90, 100, 15]
    @property
    def slash(self):
        return [-28, "Slash", 0, 70, 100, 20]
    @property
    def dragon_rage(self):
        return [-29, "Dragon Rage", 0, 40, 100, 10]
    @property
    def fire_spin(self):
        return [-30, "Fire Spin", 0, 35, 85, 15]
    @property
    def withdraw(self):
        return [-31, "Withdraw", 0, 6, 100, 40]
    @property
    def water_gun(self):
        return [-32, "Water Gun", 0, 40, 100, 25]
    @property
    def bite(self):
        return [-33, "Bite", 0, 60, 100, 25]
    @property
    def rapid_spin(self):
        return [-34, "Rapid Spin", 0, 20, 100, 40]
    @property
    def protect(self):
        return [-35, "Protect", 3, 0, 100, 10]
    @property
    def rain_dance(self):
        return [-36, "Rain Dance", 0, 0, 100, 5]
    @property
    def skull_bash(self):
        return [-37, "Skull Bash", 0, 130, 100, 10]
    @property
    def bubble(self):
        return [-38, "Bubble", 0, 20, 100, 30]
    @property
    def hydro_pump(self):
        return [-39, "Hydro Pump", 0, 120, 80, 5]
    @property
    def fury_attack(self):
        return [-40, "Fury Attack", 0, 15, 85, 20]
    @property
    def horn_attack(self):
        return [-41, "Horn Attack", 0, 65, 100, 25]
    @property
    def stomp(self):
        return [-42, "Stomp", 0, 65, 100, 20]
    @property
    def horn_drill(self):
        return [-43, "Horn Drill", 0, 0, 30, 5]
    @property
    def take_down(self):
        return [-44, "Take Down"]
    @property
    def earthquake(self):
        return [-45, "Earthquake"]
    @property
    def megahorn(self):
        return [-46, "Megahorn"]
    @property
    def curse(self):
        return [-47, "Curse"]
    @property
    def night_shade(self):
        return [-48, "Night Shade"]
    @property
    def confuse_ray(self):
        return [-49, "Confuse Ray"]
    @property
    def dream_eater(self):
        return [-50, "Dream Eater"]
    @property
    def destiny_bond(self):
        return [-51, "Destiny Bond"]
    @property
    def hypnosis(self):
        return [-52, "Hypnosis"]
    @property
    def lick(self):
        return [-53, "Lick"]
    @property
    def spite(self):
        return [-54, "Spite"]
    @property
    def shadow_ball(self):
        return [-55, "Shadow Ball"]
    @property
    def nightmare(self):
        return [-56, "Nightmare"]
    @property
    def mean_look(self):
        return [-57,"Mean Look"]
    @property
    def leer(self):
        return [-58, "Leer"]
    @property
    def twister(self):
        return [-59, "Twister"]
    @property
    def wrap(self):
        return [-60, "Wrap"]
    """
    @property
    def drago_rage(self):
        return [-61,"Drago Rage"]
    """
    @property
    def safeguard(self):
        return [-62,"Safeguard"]
    @property
    def wing_attack(self):
        return [-63, "Wing Attack"]
    @property
    def outrage(self):
        return [-64, "Outrage"]
    @property
    def hyperbeam(self):
        return [-65, "Hyperbeam"]
    @property
    def confusion(self):
        return [-66, "Confusion"]
    @property
    def disable(self):
        return [-67, "Disable"]
    @property
    def barrier(self):
        return [-68, "Barrier"]
    @property
    def mist(self):
        return [-69,"Mist"]
    @property
    def swift(self):
        return [-70, "Swift"]
    @property
    def recover(self):
        return [-71, "Recover"]
    @property
    def psychic(self):
        return [-72, "Psychic"]
    @property
    def psych_up(self):
        return [-73, "Psych Up"]
    @property
    def future_sight(self):
        return [-74,"Future Sight"]
    @property
    def amnesia(self):
        return [-75,"Amnesia"]



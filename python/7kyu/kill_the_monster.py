# https://www.codewars.com/kata/5b36137991c74600f200001b/train/python

def kill_monsters(health, monsters, damage):
    hits = 0
    tot_damage = 0
        
    while(monsters > 3):
        monsters -= 3
        tot_damage += damage
        hits += 1
        health = health - damage
        
        if (health <= 0):
            return "hero died"

    return "hits: {}, damage: {}, health: {}".format(hits, tot_damage, health)


print(kill_monsters(50, 7, 10))


"""
* clever

def kill_monsters(hp,m,dmg):
    x,y = divmod(m,3)
    hits = x - 1 + min(y,1)
    return 'hero died' if dmg * hits >= hp else f'hits: {hits}, damage: {hits * dmg}, health: {hp - hits * dmg}'
"""

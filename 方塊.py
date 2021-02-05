from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x-10,y,z-10,x+10,y-50,z+10,0)
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

while True:
    color = random.randrange(0,9)
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)
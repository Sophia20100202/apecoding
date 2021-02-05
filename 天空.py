from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

while True:
    position = mc.player.getPos()
    x = position.x + random.uniform(-20,20)
    y = position.y + 20
    z = position.z + random.uniform(-20,20)
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.5)

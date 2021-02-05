from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(0.5)
mc.postToChat("COVID-19 is coming")
x,y,z, = mc.player.getTilePos()
number = 1
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,27)
    number = number * 2
    mc.postToChat("生成了"+str(number)) 

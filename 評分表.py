from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    a = mc.getBlock(x,y-1,z)
    
    if a == 57:
        mc.postToChat("thanks for your support!")
        break
    elif a == 41:
        mc.postToChat('thank you I will try harder!')
        break
    elif a == 46:
        mc.postToChat('ok I will make it better!')
        break
        
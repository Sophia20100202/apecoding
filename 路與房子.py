from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(20):
    x,y,z = mc.player.getPos()
    x = x + i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x,y,z,x+10,y+15,z+10,57)
mc.setBlocks(x+1,y+1,z+1,x+9,y+14,z+9,0)
mc.setBlocks(x+6,y+1,z,x+6,y+2,z,0)
mc.setBlocks(x,y+8,z,x+10,y+8,z+10,57)


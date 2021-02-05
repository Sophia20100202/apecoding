from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

a = input('你是誰?')
mc.setBlocks(x,y,z,x+10,y+15,z+10,5)
mc.setBlocks(x+1,y+1,z+1,x+9,y+14,z+9,0)
mc.setBlocks(x+6,y+1,z,x+6,y+2,z,0)
mc.setBlocks(x,y+7,z,x+10,y+7,z+10,5)
mc.postToChat('Hello!'+a+'你好,我是史萊姆')
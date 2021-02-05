from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ChocoWhite = []
LittleBlue = []
Lovely = []

for i in range(1,4):
    ChocoWhite.append(2*i)
for i in range(1,4):
    LittleBlue.append(3*i)
for i in range(1,4):
    Lovely.append(4*i)
    
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,str(ChocoWhite),str(LittleBlue),str(Lovely))
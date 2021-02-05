from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

answer = randrange(0,16)
myID = mc.getPlayerEntityId('Sophia20100101')
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > [0]:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data > answer:
            mc.postToChat('你答錯囉!>"<')
        elif data < answer:
            mc.postToChat('你答錯囉!>"<')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitile(myID,'叮叮叮!答對囉!>U<')
            break
            
    
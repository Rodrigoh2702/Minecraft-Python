from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

blockType=mc.getBlock(x,y,z)
mc.postToChat(blockType==9)

#Si quieres ver si estas completamente debajo del agua,
#Crea una variable que almacene y+1 y comparala con 9 tambien

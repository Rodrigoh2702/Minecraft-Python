from mcpi.minecraft import Minecraft
mc=Minecraft.create()
blockType= input ("Enter the block you want to create: ")
blockType=int (blockType)
pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

mc.setBlock(x,y,z,blockType)

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
width=10
height=5
length=6
blockType=4
air=0
mc.setBlocks(x,y,z, x+width, y+height, z+length, blockType)
x=x+1
y=y+1
z=z+1
mc.setBlocks(x,y,z, x+width-2, y+height-2, z+length-2, air)

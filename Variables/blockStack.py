from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=5
y=91
z=25
blockType=103

mc.setBlock(x,y,z,blockType)

y=y+1
mc.setBlock(x,y,z,blockType)

y=y+1
mc.setBlock(x,y,z,blockType)

y=y+1
mc.setBlock(x,y,z,blockType)

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=20
y=88
z=26
blockType=103
mc.setBlock(x,y,z,blockType)
mc.setBlock(x,y+1,z,blockType)

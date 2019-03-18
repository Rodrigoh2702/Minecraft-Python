from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z
blocktype=10
y=y+5

mc.player.setTilePos(x,y,z)
y=y-5
mc.setBlock(x,y,z,blocktype)

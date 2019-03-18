from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

try:
    blockType=int(input("Enter the block you want to create: "))
    mc.setBlock(x,y,z,blockType)
except:
    mc.postToChat("Not a number")

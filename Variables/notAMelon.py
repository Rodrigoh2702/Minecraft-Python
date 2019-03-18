from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=5
y=91
z=25
melon=103
block=mc.getBlock(x,y,z)

noMelon=block!= melon

mc.postToChat("You need to get some food: " + str(noMelon))

# Voxel-Based-Minecraft-3D-Printer
Converts stl files to a voxel representation and prints it in Minecraft

Minecraft is a sandbox video game developed by Mojang Studios that allows players explore a blocky, procedurally generated 3D world. These blocks can be interpreted sort of like voxels as, voxels are representations of values on a grid in three-dimensional space.

The idea is that I wanted to treat minecraft as the "print bed" for 3D objects stored in stl (Standard Triangle Language) files to create those 3d objects in the world of minecraft.

![](https://www.gamersnexus.net/images/media/2012/features/voxels-vs-vertexes.png)

I did this by creating a tkinter UI that allows one to upload the file, choose the files start coordinates, and preview the build.

![](https://i.gyazo.com/6ad891a3ad707689da3a879267f5910d.png) ![](https://i.gyazo.com/c632da7e711cbe6f4267ea869641189c.png)

Once all the desired variables are filled in the player will start placing blocks in acoraance with their voxel position and scaffolding to support the blocks that are overhanging.

![](https://i.gyazo.com/c7aa7f07552d8f7d54573a065e2da655.jpg) ![](https://i.gyazo.com/4b4950ede6f128da9a72c4a09d48ced8.png)

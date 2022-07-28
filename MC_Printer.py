from tkinter import *
from tkinter import filedialog
import pyvista as pv
import Printer_Utils
import time

Voxel_main = None
file = None
rotation = 0


def Open():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.stl"),)
        )

    pathh.insert(0,tf)
    global file
    file = tf

def Preview():
    global file
    tf = file
    mesh = pv.read(tf)
    complexity = 150

    try:
        complexity = int(pvox.get())
    except:
        pass

    voxels = pv.voxelize(mesh, density=mesh.length / complexity, check_surface=False)

    global Voxel_main
    Voxel_main = voxels

    p = pv.Plotter(off_screen=True)
    p.add_mesh(Voxel_main)
    p.screenshot('voxel.png', window_size = (500,500))

    newWindow = Toplevel(ws)

    newWindow.title("Voxel Preview")
    newWindow.geometry("500x540")
    newWindow['bg'] = '#5865F2'

    canvas = Canvas(newWindow, width=500, height=500)
    canvas.pack()
    img = PhotoImage(file="voxel.png")
    canvas.create_image(250, 250, image=img)

    def RotateL():
        global rotation
        rotation = rotation + 45

        global Voxel_main
        p = pv.Plotter(off_screen=True)
        p.add_mesh(Voxel_main)
        p.camera.azimuth = rotation
        p.screenshot('voxel.png', window_size=(500, 500))

        img = PhotoImage(file="voxel.png")
        canvas.create_image(250, 250, image=img)

    def RotateR():
        global rotation
        rotation = rotation - 45

        global Voxel_main
        p = pv.Plotter(off_screen=True)
        p.add_mesh(Voxel_main)
        p.camera.azimuth = rotation
        p.screenshot('voxel.png', window_size=(500, 500))

        img = PhotoImage(file="voxel.png")
        canvas.create_image(250, 250, image=img)

    x_map_d = {}
    y_map_d = {}
    z_map_d = {}
    for item in Voxel_main.points:
        x_map_d[item[0]] = 0
        y_map_d[item[1]] = 0
        z_map_d[item[2]] = 0

    Button(newWindow, text="Rotate Left", command=RotateL).pack(padx=10, side=LEFT)
    Button(newWindow, text="Rotate Right", command=RotateR).pack(padx=10, side=RIGHT)

    temp = 'Width: ' + str(len(y_map_d)) + ' | Length: ' + str(len(x_map_d)) + ' | Height: ' + str(len(z_map_d))
    dims = Label(newWindow, text=temp, background='#5865F2')
    dims.pack(expand=True)

def Build():
    global file
    global Voxel_main
    global hollow

    time.sleep(5)

    if Voxel_main == None:
        tf = file
        mesh = pv.read(tf)
        complexity = 150

        try:
            complexity = int(pvox.get())
        except:
            pass

        voxels = pv.voxelize(mesh, density=mesh.length / complexity, check_surface=False)
        Voxel_main = voxels

    arr = Printer_Utils.Voxel2Array(Voxel_main)

    try:
        mod_x = (int(px.get()) / abs(int(px.get())))
    except:
        mod_x = 1

    try:
        mod_z = (int(pz.get()) / abs(int(pz.get())))
    except:
        mod_z = 1

    x_start = int(px.get()) + mod_x * 0.5
    y_start = int(py.get())
    z_start = int(pz.get()) + mod_z * 0.5

    Printer_Utils.Down()

    for x in range(59, arr.shape[0]):
        for z in range(0, arr.shape[1]):
            Printer_Utils.TP(x_start+x, y_start, z_start+z)
            blank_count = 0
            for y in range(0, arr.shape[2]):
                if Printer_Utils.CheckSum(arr[x,z,y:-1]):
                    pass
                else:
                    blank_count = Printer_Utils.Place(blank_count, x, y, z, arr, x_start, y_start, z_start)
                #scaf or place



ws = Tk()
ws.title("MC 3D Printer")
ws.geometry("335x190")
ws['bg']='#5865F2'


pathh = Entry(ws, width = 40)
pathh.grid(row = 0, padx=10, pady=10,column=0, columnspan=3)

Button(ws,text="Open File",command=Open).grid(row = 0, column=4, pady=10)

lv = Label(text='Voxel Complexity', background='#5865F2')
lv.grid(row=1, columnspan=1)

pvox = Entry(ws, width = 10)
pvox.insert(0,'150')
pvox.grid(row=1, column=1)

Button(ws,text="Preview",command=Preview).grid(row = 1, column=4, pady=10)

l1 = Label(text='Enter starting Coordinates', background='#5865F2')
l1.grid(row=2, columnspan=4)

lx = Label(text='X:', background='#5865F2')
ly = Label(text='Y:', background='#5865F2')
lz = Label(text='Z:', background='#5865F2')

px = Entry(ws, width = 10)
py = Entry(ws, width = 10)
pz = Entry(ws, width = 10)

lx.grid(row=3, column=0)
ly.grid(row=4, column=0)
lz.grid(row=5, column=0)
px.grid(row=3, column=1,pady=3)
py.grid(row=4, column=1)
pz.grid(row=5, column=1)

Button(ws,text="Start Build",command=Build).grid(row = 5, column=4)

ws.mainloop()

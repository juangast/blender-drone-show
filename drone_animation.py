import bpy
import math

drone_names = ["Drone_01", "Drone_02", "Drone_03", "Drone_04", "Drone_05"]
x_positions = [-4, -2, 0, 2, 4]

#take off
for i, name in enumerate(drone_names):
    drone = bpy.data.objects[name]

    # Frame 1 - On the ground
    bpy.context.scene.frame_set(1)
    drone.location = (x_positions[i], 0, 0)
    drone.keyframe_insert(data_path="location", frame=1)

    # Frame 60 - Takeoff
    bpy.context.scene.frame_set(60)
    drone.location = (x_positions[i], 0, 5)
    drone.keyframe_insert(data_path="location", frame=60)



#circle formation
radius = 4
height = 5
num_drones = len(drone_names)

for i, name in enumerate(drone_names):
    drone = bpy.data.objects[name]

    angle = (2 * math.pi / num_drones) * i

    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    bpy.context.scene.frame_set(120)
    drone.location = (x, y, height)
    drone.keyframe_insert(data_path="location", frame=120)

print("Circle formation created!")
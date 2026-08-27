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


# V  formation
expanded_positions = [
    (-6, 0, 8),
    (-3, 0, 6.5),
    (0, 0, 5),
    (3, 0, 6.5),
    (6, 0, 8)
]

for i, name in enumerate(drone_names):
    drone = bpy.data.objects[name]

    bpy.context.scene.frame_set(330)
    drone.location = expanded_positions[i]
    drone.keyframe_insert(data_path="location", frame=330)

print("V formation expanded!")


#color change
drone = bpy.data.objects["Drone_01"]
material = drone.active_material

principled = material.node_tree.nodes.get("Principled BSDF")
emission = principled.inputs["Emission Color"]

# frame 330 - Blue
bpy.context.scene.frame_set(330)
emission.default_value = (0.0, 0.3, 1.0, 1.0)
emission.keyframe_insert(data_path="default_value", frame=330)

# frame 370 - Purple
bpy.context.scene.frame_set(370)
emission.default_value = (0.8, 0.0, 1.0, 1.0)
emission.keyframe_insert(data_path="default_value", frame=370)

print("Color animation created!")


# landing
landing_positions = [-4, -2, 0, 2, 4]

for i, name in enumerate(drone_names):
    drone = bpy.data.objects[name]

    # return above landing position
    bpy.context.scene.frame_set(410)
    drone.location = (landing_positions[i], 0, 5)
    drone.keyframe_insert(data_path="location", frame=410)

    # landing
    bpy.context.scene.frame_set(470)
    drone.location = (landing_positions[i], 0, 0)
    drone.keyframe_insert(data_path="location", frame=470)

print("Landing created!")
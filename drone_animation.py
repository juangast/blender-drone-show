import bpy

drone_names = ["Drone_01", "Drone_02", "Drone_03", "Drone_04", "Drone_05"]
x_positions = [-4, -2, 0, 2, 4]

for i, name in enumerate(drone_names):
    drone = bpy.data.objects[name]

    # frame 1 on the floor
    bpy.context.scene.frame_set(1)
    drone.location = (x_positions[i], 0, 0)
    drone.keyframe_insert(data_path="location", frame=1)

    # frame 60 now all up
    bpy.context.scene.frame_set(60)
    drone.location = (x_positions[i], 0, 5)
    drone.keyframe_insert(data_path="location", frame=60)

print("Now all the drones are taking off")
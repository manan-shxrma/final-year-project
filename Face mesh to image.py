import matplotlib.pyplot as plt
import trimesh
import numpy as np
import pyrender
import imageio

def render_image(obj_path, camera_center, camera_pose):
    mesh = trimesh.load_mesh(obj_path)
    scene = pyrender.Scene()
    scene.add(pyrender.Mesh.from_trimesh(mesh))
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)

    scene.add(camera, pose=camera_pose)
    light1 = pyrender.SpotLight(color=np.ones(3), intensity=3.0,
                                innerConeAngle=np.pi/10.0)
    light2 = pyrender.SpotLight(color=np.ones(3), intensity=3.0,
                                innerConeAngle=np.pi/10.0, outerConeAngle=np.pi/5.0)
    light3 = pyrender.PointLight(color=np.ones(3), intensity=1.0)
    scene.add(light1, pose=camera_pose)
    scene.add(light2, pose=np.eye(4))
    scene.add(light3, pose=np.eye(4))

    renderer = pyrender.OffscreenRenderer(640, 640)
    color, depth = renderer.render(scene, flags=pyrender.RenderFlags.RGBA)
    color = color.copy()
    color[depth == 0] = 0

    return color


"""
example usage 
obj_path = "face-meshes/5-36-in_mesh.obj"
camera_center = np.array([0, 0, 0]) 
camera_pose = np.array([
    [1, 0,  0, camera_center[0]],
    [0, 0, -1, camera_center[1]],
    [0, 1,  0, camera_center[2] + 100],
    [0, 0,  0, 1]
])  

rendered_image = render_image(obj_path, camera_center, camera_pose)
imageio.imwrite('rendered_image.png', rendered_image)
"""

from UnityEngine import GameObject, Camera, Texture2D, Rect, Quaternion
from System.IO import File
from objreader import ObjReader


class RenderToImage:
    def Start(self):
        # Path to save the rendered image
        imagePath = "RenderedImage.png"
        # Width and height of the rendered image
        imageWidth = 1920
        imageHeight = 1080

        # Load the 3D model from the .obj file
        objFilePath = "face-meshes/5-36-in_mesh.obj"  # Replace "YourModel.obj" with the path to your .obj file
        objReader = ObjReader.read(objFilePath)

        # Create GameObjects for the model's meshes
        for mesh in objReader.meshes:
            gameObject = GameObject.CreatePrimitive(mesh.type)
            gameObject.GetComponent(MeshFilter).mesh = mesh.mesh

        # Set up the camera to render the model
        renderCamera = Camera.main

        # Set camera properties as desired
        # For example, set camera position and rotation
        renderCamera.transform.position = Vector3(0, 1, -10)
        renderCamera.transform.rotation = Quaternion.Euler(0, 180, 0)

        # Render the scene to the render texture
        renderCamera.Render()

        # Create a new texture to store the rendered image
        renderedTexture = Texture2D(imageWidth, imageHeight, TextureFormat.RGB24, False)

        # Read pixels from the render texture and apply to the new texture
        renderedTexture.ReadPixels(Rect(0, 0, imageWidth, imageHeight), 0, 0)
        renderedTexture.Apply()

        # Encode the texture to a PNG file
        bytes = renderedTexture.EncodeToPNG()

        # Save the PNG file
        File.WriteAllBytes(imagePath, bytes)



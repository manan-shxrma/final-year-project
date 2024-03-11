using UnityEngine;
using System.Collections;

public class Render3DModel : MonoBehaviour
{

    string[] args = System.Environment.GetCommandLineArgs();
    if (args.Length > 1)
    {
        objPath = args[1]; // Set the .obj file path from the command line argument
    }
    
    public string objPath = "C:\Users\Mohit\PycharmProjects\Intoxication Detection\face-meshes\5-36-in_mesh.obj"; // Path to your .obj file
    public int imageWidth = 1024; // Width of the output image
    public int imageHeight = 768; // Height of the output image
    public string imagePath = "Assets/renderedImageC#.png"; // Path to save the output image

    void Start()
    {
        // Load the .obj file
        var obj = new OBJLoader().Load(objPath);

        // Add the object to the scene
        Instantiate(obj, Vector3.zero, Quaternion.identity);

        // Create a new RenderTexture
        var rt = new RenderTexture(imageWidth, imageHeight, 24);
        GetComponent<Camera>().targetTexture = rt;

        // Create a new Texture2D and read the RenderTexture into it
        var tex = new Texture2D(imageWidth, imageHeight, TextureFormat.RGB24, false);
        RenderTexture.active = rt;
        tex.ReadPixels(new Rect(0, 0, imageWidth, imageHeight), 0, 0);
        tex.Apply();

        // Convert the Texture2D to a .png
        var bytes = tex.EncodeToPNG();

        // Save the .png
        System.IO.File.WriteAllBytes(imagePath, bytes);
    }
}


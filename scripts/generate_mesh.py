import json
import numpy as np
import open3d as o3d

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def extract_points(data):
    points = []
    for obj in data.get("objects", []):
        if obj and "polygon" in obj:
            for poly in obj["polygon"]:
                ymin, ymax = poly["Ymin"], poly["Ymax"]
                x_vals, z_vals = poly["X"], poly["Z"]
                if len(x_vals) == len(z_vals):
                    for i in range(len(x_vals)):
                        points.append([x_vals[i], ymin, z_vals[i]])
                        points.append([x_vals[i], ymax, z_vals[i]])
    return np.array(points)

def create_mesh(points):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    
    # Estimate normals for surface reconstruction
    point_cloud.estimate_normals()
    
    # Perform Poisson surface reconstruction
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(point_cloud, depth=9)
    return mesh

def main():
    # json_data = load_json("index.json")
    json_data = load_json("C:/Project Deep Learning/data/SUNRGBD/kv1/b3dodata/img_0063/annotation3D/index.json")
    points = extract_points(json_data)
    if len(points) == 0:
        print("No 3D points found in the dataset.")
        return
    
    mesh = create_mesh(points)
    o3d.io.write_triangle_mesh("C:/Project Deep Leraning/outputs/output_mesh.ply", mesh)
    o3d.visualization.draw_geometries([mesh])

if __name__ == "__main__":
    main()
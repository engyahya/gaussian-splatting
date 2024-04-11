import numpy as np
import open3d as o3d
from plyfile import PlyData, PlyElement

def storePly(path, xyz, rgb):
    # Define the dtype for the structured array
    dtype = [('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
            ('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4'),
            ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]
    
    normals = np.zeros_like(xyz)

    elements = np.empty(xyz.shape[0], dtype=dtype)
    attributes = np.concatenate((xyz, normals, rgb), axis=1)
    elements[:] = list(map(tuple, attributes))

    # Create the PlyData object and write to file
    vertex_element = PlyElement.describe(elements, 'vertex')
    ply_data = PlyData([vertex_element])
    ply_data.write(path)



def generate_sphere_points(radius, point_spacing):
    # Create spherical coordinates
    phi = np.arange(0, np.pi, point_spacing)
    theta = np.arange(0, 2 * np.pi, point_spacing)
    
    # Convert spherical coordinates to Cartesian coordinates
    phi, theta = np.meshgrid(phi, theta)
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    
    # Flatten the coordinates to get a list of points
    points = np.vstack((x.flatten(), y.flatten(), z.flatten())).T
    
    return points

def main():
    # Parameters
    radius = 0.2
    point_spacing = 0.1
    color = [0, 0, 0]  # Black color
    
    # Generate points on the surface of the sphere
    points = generate_sphere_points(radius, point_spacing)
    
    # Create PointCloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(np.tile(color, (len(points), 1)))
    
    # Save the PointCloud as a .pcd file
    o3d.io.write_point_cloud("sphere_points.pcd", pcd)


    output_ply_file = "points3D.ply"
    xyz = np.asarray(pcd.points)
    rgb = np.asarray(pcd.colors) * 255
    storePly(output_ply_file, xyz, rgb)

if __name__ == "__main__":
    main()

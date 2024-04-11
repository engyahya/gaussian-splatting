import open3d as o3d
import numpy as np
from plyfile import PlyData, PlyElement
import argparse

def get_args_from_command_line():
    parser = argparse.ArgumentParser(description='The argument parser of the runner')
    parser.add_argument('-s','--input', help='file_name',  type=str)

    args = parser.parse_args()
    return args

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


def convert_pcd_to_ply(pcd_file, ply_file):
    # Read the .pcd file+
    args = get_args_from_command_line()
    
    point_cloud = o3d.io.read_point_cloud(args.input)

    # Save the point cloud in .ply format
    o3d.io.write_point_cloud(ply_file, point_cloud)

if __name__ == "__main__":
    # Specify the input .pcd file and output .ply file
    #input_pcd_file = "1a4ef4a2a639f172f13d1237e1429e9e.pcd"
    # take the first part of the name before the dot

    args = get_args_from_command_line()
    input_pcd_file = args.input
    

    output_ply_file = input_pcd_file.split(".")[0] + ".ply"

    #output_ply_file = "points3D.ply"


    point_cloud = o3d.io.read_point_cloud(input_pcd_file)
    # downsample the point_cloud 
    voxel_size = 0.35  # Adjust the voxel size according to your requirements
    point_cloud = point_cloud.voxel_down_sample(voxel_size)
    print ("point_cloud")
    #print (point_cloud.shape)
    


    
     

    xyz = np.asarray(point_cloud.points)
    print ("xyz")
    print (xyz.shape)
    rgb = np.zeros_like(xyz)
    #rgb = np.asarray(point_cloud.colors) * 255
    storePly(output_ply_file, xyz, rgb)

    # Convert .pcd to .ply
    #convert_pcd_to_ply(input_pcd_file, output_ply_file)

    print(f"Conversion complete. Point cloud saved to {output_ply_file}")
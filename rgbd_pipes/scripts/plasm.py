#!/usr/bin/env python
import sys
import ecto
import ecto_ros
import ecto_ros.ecto_sensor_msgs as ecto_sensor_msgs
from ecto_pcl import *

from rgbd_pipes.utils import get_cloud_msg_pub, get_cloud_msg_sub, msg2cloud, cloud2msg, nan_filter

def generate_graph(in_topic, out_topic):
    cloud_sub           = get_cloud_msg_sub(in_topic)
    cloud_pub           = get_cloud_msg_pub(out_topic)
    voxel_grid          = VoxelGrid('voxel_grid', leaf_size=0.05)
    normals             = NormalEstimation('normals', k_search=0, radius_search=0.2)
    planar_segmentation = SACSegmentationFromNormals('planar_segmentation', model_type=SACMODEL_NORMAL_PLANE, eps_angle=0.09, distance_threshold=0.1)
    project_inliers     = ProjectInliers('project_inliers', model_type=SACMODEL_NORMAL_PLANE)
    convex_hull         = ConvexHull('convex_hull')

    graph = [cloud_sub[:] >> msg2cloud[:],
             msg2cloud[:] >> voxel_grid[:],
             voxel_grid[:] >> normals[:],
             voxel_grid[:] >> planar_segmentation['input'],
             normals[:] >> planar_segmentation['normals'],
             voxel_grid[:] >> project_inliers['input'],
             planar_segmentation['model'] >> project_inliers['model'],
             project_inliers[:] >> nan_filter[:],
             nan_filter[:] >> convex_hull['input']
             ]

    extract_stuff = ExtractPolygonalPrismData('extract_stuff', height_min=0.01, height_max= 0.2)
    extract_indices = ExtractIndices('extract_indices', negative=False)
    extract_clusters = EuclideanClusterExtraction('extract_clusters', min_cluster_size=50, cluster_tolerance=0.005)
    colorize = ColorizeClusters('colorize')
    merge = MergeClouds('merge')

    graph += [
              msg2cloud[:] >> extract_stuff['input'],
              convex_hull[:] >> extract_stuff['planar_hull'],
              extract_stuff[:] >> extract_indices['indices'],
              msg2cloud[:] >> extract_indices['input'],

              extract_indices[:] >> extract_clusters['input'],
              extract_clusters[:] >> colorize['clusters'],
              extract_indices[:] >> colorize['input'],

              msg2cloud[:] >> merge['input'],
              colorize[:] >> merge['input2'],
              merge[:] >> cloud2msg[:],
              cloud2msg[:] >> cloud_pub[:]
            ]
    return graph

def generate_plasm(graph):
    plasm = ecto.Plasm()
    plasm.connect(graph)

    ecto.view_plasm(plasm)

    return plasm

if __name__ == '__main__':
    ecto_ros.init(sys.argv, "ecto_pcl_demo")

    graph = generate_graph('/camera/depth_registered/points', 'new_points')
    plasm = generate_plasm(graph)

    from ecto.opts import doit
    doit(plasm)


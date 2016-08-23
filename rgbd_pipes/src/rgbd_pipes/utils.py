
import ecto_ros.ecto_sensor_msgs as ecto_sensor_msgs
import ecto_pcl_ros
import ecto_pcl

def get_cloud_msg_sub(topic):
    return ecto_sensor_msgs.Subscriber_PointCloud2('cloud_sub', topic_name=topic)

def get_cloud_msg_pub(topic):
    return ecto_sensor_msgs.Publisher_PointCloud2('cloud_pub', topic_name=topic)

msg2cloud = ecto_pcl_ros.Message2PointCloud('msg2cloud', format=ecto_pcl.XYZRGB)
cloud2msg = ecto_pcl_ros.PointCloud2Message('cloud2msg')

nan_filter = ecto_pcl.PassThrough('nan_removal')

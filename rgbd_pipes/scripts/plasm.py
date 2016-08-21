#!/usr/bin/env python
import ecto
from ecto_image_pipeline.io.source.ros import OpenNISubscriber
from ecto_pcl import CloudViewer

def generate_plasm(depth_image_topic):
    #openni_subscriber = OpenNISubscriber(depth_image_topic=depth_image_topic)
    openni_subscriber = OpenNISubscriber()
    cloud_viewer = CloudViewer('Cloud Display')

    plasm = ecto.Plasm()
    plasm.connect(openni_subscriber[:] >> cloud_viewer[:])

    return plasm

if __name__ == '__main__':

    plasm = generate_plasm('points')
    print plasm.viz()

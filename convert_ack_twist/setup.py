import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'convert_ack_twist'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='masteredwon',
    maintainer_email='edwinchung11@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'convert_msg = convert_ack_twist.ackermann_to_twist:main',
            'ack_publisher = convert_ack_twist.ackermann_pub:main',
        ],
    },
)

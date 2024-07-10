from setuptools import setup
import os
from glob import glob

package_name = 'py_0711'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rlmodel',
    maintainer_email='rlmodel@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stop = py_0711.stop_motor:main',
            'start = py_0711.start_motor:main',
            'emergency = py_0711.emergency_stop:main',
        
        ],
    },
)

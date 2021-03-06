import os
from distutils.core import setup

package_name = "yt_extname"
version = '0.1'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()
setup(name=package_name,
      version=version,
      description=("Name of the extension"),
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
          ("Topic :: Software Development :: Libraries :: Python Modules"),
      ],
      keywords='data',
      author='Your Name Here <youremail@he.re>',
      license='BSD',
      package_dir={package_name: package_name},
      packages=[package_name],
      install_requires=["yt"],
      url="http://yoururl/",
      author_email="youremail@he.re",
)

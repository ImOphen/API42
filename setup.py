from distutils.core import setup
setup(
  name = 'API42',
  packages = ['API42'],
  version = '0.0.5.3',
  license='MIT',
  description = 'Wrapper for the 42 intra API',
  author = 'Ayman Touhami',
  author_email = 'itsophen@gmail.com',
  url = 'https://github.com/ImOphen/API42',
  download_url = 'https://github.com/ImOphen/API42/archive/refs/tags/v0.0.5.3.tar.gz',
  keywords = ['42', 'Intra', 'API'],
  install_requires=[ 
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',    
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)

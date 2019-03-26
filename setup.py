from distutils.core import setup
setup(
  name = 'hdflow',         # How you named your package folder (MyLib)
  packages = ['hdflow'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Convert CSV netflow to HDF5 in parallel.',   # Give a short description about your library
  author = 'William Reus',                   # Type in your name
  author_email = 'reuster986@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/reuster986/hdflow',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'h5py',
	  'pandas',
	  'numpy',
	  'tqdm'
      ],
  scripts=['hdflow/scripts/csv2hdf']
)

import os

from setuptools import setup, find_packages



setup(
	name='rose2',
	version='1.0.0',
	description='ROSE2 python package',
	long_description='PROGRAM TO STITCH TOGETHER REGIONS TO FORM ENHANCERS, MAP READ DENSITY TO STITCHED REGIONS,AND RANK ENHANCERS BY READ DENSITY TO DISCOVER SUPER-ENHANCERS',
	url='https://github.com/linlabbcm/rose2',
	download_url = 'https://github.com/linlabbcm/rose2/tarball/v1.0.0',
	

	classifiers=[],

	keywords=['bioinformatics','super-enhancers'],

	packages=find_packages(),

	install_requires=['numpy>=1.8.2'],

	extras_require={},

	data_files=[
		('annotation', [
			'annotation/danRer7_refseq.ucsc',
			'annotation/hg18_refseq.ucsc',
			'annotation/hg19_refseq.ucsc',
			'annotation/hg19.chrom.sizes',
			'annotation/hg38_refseq.ucsc',
			'annotation/mm8_refseq.ucsc',
			'annotation/mm9_refseq.ucsc',
			'annotation/mm10_refseq.ucsc',
			'annotation/mm10.chrom.sizes',
			'annotation/rn4_refseq.ucsc',
			'annotation/ucsc_chromSize.txt',
		])
	],

	scripts=['scripts/ROSE2_callSuper.R', 'scripts/ROSE2_stitchOpt.R'],

	entry_points={
	    'console_scripts': [
	        'rose2=rose2:main',
	        ]
	    },

)
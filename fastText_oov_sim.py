from gensim.models import KeyedVectors
from subprocess import call, run, PIPE
import subprocess
import sys
import numpy as np

model=None

def oov(inword):
	global model

	p = run(['./fasttext', 'print-word-vectors', sys.argv[1]], stdout=PIPE, input=inword.encode('utf8'))
	res =p.stdout
  
	res=res.decode('utf-8')	
	vec=[]
	res = res.replace('\n', '')
	res = res.split(' ')
	for i,e in enumerate(res):
		if i==0:
			continue
		if e=='':
			continue
		vec.append(float(e))

	npvec = np.asarray(vec)
	print(inword)
	print(model.similar_by_vector(npvec))

def _start_shell(local_ns=None):
	# An interactive shell is useful for debugging/development.
	import IPython
	user_ns = {}
	if local_ns:
		user_ns.update(local_ns)
	user_ns.update(globals())
	IPython.start_ipython(argv=[], user_ns=user_ns)

def main():
	global model
	print('# Usage: python fast_oov_sim.py model.bin model.vec')
	if len(sys.argv) < 3:
		print('-Not enough arguments : Expected 2 .bin, .vec')
		sys.exit()
	print('Loading vector ...')
	model = KeyedVectors.load_word2vec_format(sys.argv[2])
	print('#Test E.g.,\n#In [0]: oov("notebook")\n#In [1]: oov("bicycle")')

	_start_shell(locals())

if __name__=="__main__":
	main()


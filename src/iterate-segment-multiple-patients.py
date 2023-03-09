
import os
from subprocess import call 
import sys , getopt
import time

global srcrootdir
global targetrootdir

if __name__ == '__main__' :
	argv = sys.argv
	srcrootdir = ''
	targetrootdir = ''
	try : 
		opts , _ = getopt.getopt ( argv [ 1 : ] , 's:t:' , ['srcrootdir=' , 'targetrootdir=' ] )
	except getopt.GetoptError : 
		print ( 'err' ) ; sys.exit( 2 )
	for opt , arg in opts : 
		if opt in ( '--srcrootdir' ) : srcrootdir = arg
		if opt in ( '--targetrootdir' ) : targetrootdir = arg

	FILENAME = argv[ 0 ]	
	if len ( srcrootdir) < 1 or len ( targetrootdir ) < 1 :
		print ( 'syntax' , FILENAME , '--srcrootdir=[]', '--targetrootdir=[]' ) ; sys.exit(2)
	if ( os.path.exists ( srcrootdir) ) : pass
	else : print ( 'srcdir non existent!!!' ) ; sys.exit(2)
		
	list0 = os.listdir ('.') # print ( 'list', list0  )
	listonlydirs = list ( filter(lambda x: os.path.isdir( x ) , list0 ) ) # print ( 'only dirs' , listonlydirs) 
	n_dirs_processed = 0
	for dirname in listonlydirs :
		print ( dirname ) 
#		os.system ( 'python3 
		timestamp = time.time()
		call ( [ 'python3' , '/home/ubuntu/anyou-20230306/src/CTLungSegmentor-takes-one-folder.py' , '--srcdcmvoldir='+srcrootdir+'/'+dirname , '--targetrootdir='+targetrootdir ] )
		curtime = time.time()
		print ( 'delta time' , curtime - timestamp )
		print ( 'n_dirs_processed: ' , n_dirs_processed )  
		curtime = timestamp


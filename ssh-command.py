import subprocess
import string
#ret = subprocess.call(["ssh", "appuas@puppetmaster.lsops.org", "ls"]);
filename='nodes.txt'
with open(filename) as file_object: #lreading file
		for host in file_object:
			host=host.strip()
			prog = subprocess.Popen(["ssh", "appuas@%s" %host, '-o', 'StrictHostKeyChecking=no', "host",], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
			out, err  = prog.communicate()
			print "%s : %s" %(host,out)


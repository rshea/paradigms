import subprocess

class module_ls: 
    def index(self): 
        proc = subprocess.Popen("ls", stdout=subprocess.PIPE) 
        output = proc.stdout.read() 
        return ''' 
            <p>The output of ls is</p>'''+output+''' 
            <p>[<a href="../">Return</a>]</p> 
        ''' 
    index.exposed = True

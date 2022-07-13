import subprocess
print ("runnning python code through docker")
inputfile = 'input.txt'
gotoutputfile= 'gotoutput.txt'
codefile ='hello.java'
codefilename = 'hello.java'
codename = 'hello'
complete= subprocess.run(f'docker run -d java tail -f /dev/null',capture_output=True)
containerId = complete.stdout.decode()[:-1]
subprocess.run(f'docker cp {codefile} {containerId}:/{codefilename}')
subprocess.run(f'docker exec {containerId} javac {codefilename} ')

subprocess.run(f'docker cp {inputfile} {containerId}:/input.txt')

subprocess.run(f'docker exec -it {containerId} sh -c "java {codename} <input.txt> output.txt"')
subprocess.run(f'docker cp {containerId}:/output.txt {gotoutputfile}')

subprocess.run(f'docker rm -f {containerId}')

# subprocess.run(f'py {file} <{inputfile}> {outputfile}',shell=True)
# docker cp input.txt a4940d7739bb:/input.txt 
# docker cp code.py a4940d7739bb:/code.py 
# docker exec -it a4940d7739bb sh -c "python code.py <input.txt> output.txt"
# docker cp a4940d7739bb:/output.txt gotoutput.txt
import os
import subprocess

def main():
    # Forking a child process
    child_pid = os.fork()
    
    if child_pid == 0:
        print("Child Process: PID =", os.getpid())
        os.execlp('ls', 'ls', '-l')
    else:
        print("Parent Process: PID =", os.getpid())
        os.wait()
        print("Child process has finished execution.")

if __name__ == "__main__":
    main()

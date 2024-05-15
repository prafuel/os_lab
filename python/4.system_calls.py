import os
import sys

def process_system_calls():
    pid = os.fork()
    if pid < 0:
        print("Fork failed")
        return
    elif pid == 0:
        # Child process
        print(f"Child process: PID = {os.getpid()}")
        os._exit(0)
    else:
        # Parent process
        print(f"Parent process: PID = {os.getpid()}, Child PID = {pid}")
        os.wait()

def file_system_calls():
    filename = "hello.txt"
    try:
        # Create and open a new file
        fd = os.open(filename, os.O_CREAT | os.O_RDWR, 0o600)

        # Write data to the file
        written = os.write(fd, b"Hello, this is a sample file!")
        if written < 0:
            print("Write failed")
        
        # Read data from the file
        os.lseek(fd, 0, os.SEEK_SET)
        buffer = os.read(fd, 100)
        if buffer:
            print(f"Read from file: {buffer.decode()}")
        
        # Close the file
        os.close(fd)

        # Remove the file
        os.unlink(filename)
    except OSError as e:
        print(f"Error: {e}")

def communication_system_calls():
    try:
        r, w = os.pipe()
    except OSError as e:
        print(f"Pipe creation failed: {e}")
        return

    pid = os.fork()
    if pid < 0:
        print("Fork failed")
        return
    elif pid == 0:
        # Child process - write to the pipe
        os.close(r)
        message = b"Hello from the child process!"
        written = os.write(w, message)
        os.close(w)
        if written < 0:
            print("Write failed")
        os._exit(0)
    else:
        # Parent process - read from the pipe
        os.close(w)
        buffer = os.read(r, 100)
        os.close(r)
        if buffer:
            print(f"Message received from child process: {buffer.decode()}")
        os.wait()

def information_system_calls():
    filename = "hello.txt"
    try:
        # Create a temporary file for demonstration purposes
        with open(filename, "w") as f:
            f.write("Temporary file content")

        # Get file information
        file_stat = os.stat(filename)
        print(f"Information about '{filename}':")
        print(f"File Size: {file_stat.st_size} bytes")
        print(f"Number of Links: {file_stat.st_nlink}")
        print(f"File inode: {file_stat.st_ino}")
        print(f"File Permissions: {oct(file_stat.st_mode)}")
        print(f"File UID: {file_stat.st_uid}")
        print(f"File GID: {file_stat.st_gid}")
        
        # Clean up temporary file
        os.remove(filename)
    except OSError as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Process related system calls")
        print("2. File related system calls")
        print("3. Communication system calls")
        print("4. Information related system calls")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            process_system_calls()
        elif choice == 2:
            file_system_calls()
        elif choice == 3:
            communication_system_calls()
        elif choice == 4:
            information_system_calls()
        elif choice == 5:
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

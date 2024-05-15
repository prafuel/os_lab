#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t child_pid;

    // Forking a child process
    child_pid = fork();

    if (child_pid == 0) {
        printf("Child Process: PID = %d\n", getpid());
        execlp("ls", "ls", "-l", NULL);
    } else {
        printf("Parent Process: PID = %d\n", getpid());
        wait(NULL);
        printf("Child process has finished execution.\n");
    }

    return 0;
}
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <unistd.h>

sem_t empty, full;
pthread_mutex_t mutex;
int buffer[5];
int count = 0;

void *producer(void *arg) {
    long int num = (long int)arg;

    sem_wait(&empty);
    pthread_mutex_lock(&mutex);

    buffer[count] = num * rand()%1000 +1;
    printf("\n Producer %ld produced: %d", num + 1, buffer[count]);
    printf("\n");
    int i;
    for(i=0;i<5;i++){
        printf("%d\n",buffer[i]);
    }
    count++;
    sleep(1);

    pthread_mutex_unlock(&mutex);
    sem_post(&full);
    pthread_exit(NULL);
}

void *consumer(void *arg) {
    long int num = (long int)arg;

    sem_wait(&full);
    pthread_mutex_lock(&mutex);
    count--;
    printf("\n Consumer %ld consumed: %d", num+ 1, buffer[count]);
    buffer[count] = 0;
    printf("\n");
    int i;
    for(i=0;i<5;i++){
        printf("%d\n",buffer[i]);
    }
    sleep(1);

    pthread_mutex_unlock(&mutex);
    sem_post(&empty);
    pthread_exit(NULL);
}

int main() {
    int nt = 0;
    unsigned long int i;

    printf("Enter total number of threads to create: ");
    scanf("%d", &nt);

    int num_producer = nt / 2 + 1;
    int num_consumer = nt - num_producer;
    pthread_t producers[num_producer];
    pthread_t consumers[num_consumer];

    sem_init(&empty, 0, 5);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);
    srand(time(0));
    for (i = 0; i < num_producer; i++) {
        pthread_create(&producers[i], NULL, producer, (void *)i);
    }
    for (i = 0; i < num_consumer; i++) {
        pthread_create(&consumers[i], NULL, consumer, (void *)i);
    }
    for (i = 0; i < num_producer; i++) {
        pthread_join(producers[i], NULL);
    }
    for (i = 0; i < num_consumer; i++) {
        pthread_join(consumers[i], NULL);
    }
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    return 0;
}
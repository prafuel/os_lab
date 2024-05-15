#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MATRIX_SIZE 3

// Example matrices
int matrix_A[MATRIX_SIZE][MATRIX_SIZE] = {{1, 2, 3},
                                          {4, 5, 6},
                                          {7, 8, 9}};

int matrix_B[MATRIX_SIZE][MATRIX_SIZE] = {{9, 8, 7},
                                          {6, 5, 4},
                                          {3, 2, 1}};

int result_addition[MATRIX_SIZE][MATRIX_SIZE] = {{0, 0, 0},
                                                  {0, 0, 0},
                                                  {0, 0, 0}};

int result_subtraction[MATRIX_SIZE][MATRIX_SIZE] = {{0, 0, 0},
                                                     {0, 0, 0},
                                                     {0, 0, 0}};

int result_multiplication[MATRIX_SIZE][MATRIX_SIZE] = {{0, 0, 0},
                                                        {0, 0, 0},
                                                        {0, 0, 0}};

// Function to perform matrix addition
void *matrix_addition(void *arg) {
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            result_addition[i][j] = matrix_A[i][j] + matrix_B[i][j];
        }
    }
    pthread_exit(NULL);
}

// Function to perform matrix subtraction
void *matrix_subtraction(void *arg) {
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            result_subtraction[i][j] = matrix_A[i][j] - matrix_B[i][j];
        }
    }
    pthread_exit(NULL);
}

// Function to perform matrix multiplication
void *matrix_multiplication(void *arg) {
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            for (int k = 0; k < MATRIX_SIZE; k++) {
                result_multiplication[i][j] += matrix_A[i][k] * matrix_B[k][j];
            }
        }
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t thread_addition, thread_subtraction, thread_multiplication;

    // Creating threads
    pthread_create(&thread_addition, NULL, matrix_addition, NULL);
    pthread_create(&thread_subtraction, NULL, matrix_subtraction, NULL);
    pthread_create(&thread_multiplication, NULL, matrix_multiplication, NULL);

    // Waiting for all threads to finish
    pthread_join(thread_addition, NULL);
    pthread_join(thread_subtraction, NULL);
    pthread_join(thread_multiplication, NULL);

    // Displaying results
    printf("Matrix Addition:\n");
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            printf("%d ", result_addition[i][j]);
        }
        printf("\n");
    }

    printf("\nMatrix Subtraction:\n");
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            printf("%d ", result_subtraction[i][j]);
        }
        printf("\n");
    }

    printf("\nMatrix Multiplication:\n");
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            printf("%d ", result_multiplication[i][j]);
        }
        printf("\n");
    }

    return 0;
}

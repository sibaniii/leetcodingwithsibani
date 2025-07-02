#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int q1[MAX_SIZE], front1, rear1;
    int q2[MAX_SIZE], front2, rear2;
} MyStack;

MyStack* myStackCreate() {
    MyStack* stack = (MyStack*)malloc(sizeof(MyStack));
    stack->front1 = 0;
    stack->rear1 = -1;
    stack->front2 = 0;
    stack->rear2 = -1;
    return stack;
}

bool isEmptyQueue(int front, int rear) {
    return front > rear;
}

void enqueue(int q[], int *rear, int val) {
    (*rear)++;
    q[*rear] = val;
}

int dequeue(int q[], int *front) {
    return q[(*front)++];
}

void myStackPush(MyStack* obj, int x) {
    enqueue(obj->q2, &obj->rear2, x);

    while (!isEmptyQueue(obj->front1, obj->rear1)) {
        enqueue(obj->q2, &obj->rear2, dequeue(obj->q1, &obj->front1));
    }

    // Copy q2 -> q1
    for (int i = 0; i <= obj->rear2; i++) {
        obj->q1[i] = obj->q2[i];
    }

    obj->front1 = 0;
    obj->rear1 = obj->rear2;

    // Reset q2
    obj->front2 = 0;
    obj->rear2 = -1;
}

int myStackPop(MyStack* obj) {
    if (isEmptyQueue(obj->front1, obj->rear1)) return -1;
    return dequeue(obj->q1, &obj->front1);
}

int myStackTop(MyStack* obj) {
    if (isEmptyQueue(obj->front1, obj->rear1)) return -1;
    return obj->q1[obj->front1];
}

bool myStackEmpty(MyStack* obj) {
    return isEmptyQueue(obj->front1, obj->rear1);
}

void myStackFree(MyStack* obj) {
    free(obj);
}

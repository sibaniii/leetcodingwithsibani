#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int s1[MAX_SIZE];
    int s2[MAX_SIZE];
    int top1;
    int top2;
} MyQueue;

MyQueue* myQueueCreate() {
    MyQueue* q = (MyQueue*)malloc(sizeof(MyQueue));
    q->top1 = -1;
    q->top2 = -1;
    return q;
}

// Stack helpers
void pushStack(int* stack, int* top, int value) {
    (*top)++;
    stack[*top] = value;
}

int popStack(int* stack, int* top) {
    return stack[(*top)--];
}

int peekStack(int* stack, int top) {
    return stack[top];
}

bool isEmptyStack(int top) {
    return top == -1;
}

// Queue methods
void myQueuePush(MyQueue* obj, int x) {
    pushStack(obj->s1, &obj->top1, x);
}

int myQueuePop(MyQueue* obj) {
    if (isEmptyStack(obj->top2)) {
        while (!isEmptyStack(obj->top1)) {
            pushStack(obj->s2, &obj->top2, popStack(obj->s1, &obj->top1));
        }
    }
    return popStack(obj->s2, &obj->top2);
}

int myQueuePeek(MyQueue* obj) {
    if (isEmptyStack(obj->top2)) {
        while (!isEmptyStack(obj->top1)) {
            pushStack(obj->s2, &obj->top2, popStack(obj->s1, &obj->top1));
        }
    }
    return peekStack(obj->s2, obj->top2);
}

bool myQueueEmpty(MyQueue* obj) {
    return isEmptyStack(obj->top1) && isEmptyStack(obj->top2);
}

void myQueueFree(MyQueue* obj) {
    free(obj);
}

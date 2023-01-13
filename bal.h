#ifndef BAL_H
#define BAL_H

#include <pthread.h>
  
typedef struct s_bal_t
{
  int data;
  pthread_mutex_t mutex;
  pthread_cond_t cond;
  unsigned int full;
} * bal_t;

bal_t bal_create();
void bal_destroy(bal_t bal);
void bal_put(bal_t bal, int data);
int bal_get(bal_t bal);

#endif
#include "bal.h"
#include <malloc.h>

bal_t bal_create()
{
  bal_t bal = malloc(sizeof(struct s_bal_t));
  bal->data = 0;
  bal->full = 0;
  pthread_mutex_init(&(bal->mutex), NULL);
  pthread_cond_init(&(bal->cond), NULL);
  return bal;
}

void bal_destroy(bal_t bal)
{
  pthread_mutex_destroy(&(bal->mutex));
  pthread_cond_destroy(&(bal->cond));
  free(bal);
}

void bal_put(bal_t bal, int data)
{
  pthread_mutex_lock(&(bal->mutex));
  bal->data = data;
  bal->full = 1;
  pthread_cond_signal(&(bal->cond));
  pthread_mutex_unlock(&(bal->mutex));
}

int bal_get(bal_t bal)
{
  int data;

  pthread_mutex_lock(&(bal->mutex));

  while (!bal->full)
  {
    pthread_cond_wait(&(bal->cond), &(bal->mutex));
  }

  data = bal->data;
  bal->full = 0;

  pthread_mutex_unlock(&(bal->mutex));

  return data;
}
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>

pthread_mutex_t locked;

int hours, min, sec;

void *func1()  {
	pthread_mutex_lock(&locked);
	while(1) {
		
		sec = sec + 1;
	}
	pthread_mutex_unlock(&locked);
}

void *func2()  {
	pthread_mutex_lock(&locked);
	while(1){
		
		if(sec == 60){
			min = min + 1;
			sec = 0;
		}
		
	}
	pthread_mutex_unlock(&locked);
}

void *func3()  {
	pthread_mutex_lock(&locked);
	while(1){
		
		if(min == 60){
			if(hours == 23){
				hours = 0;
			}
			else{
				hours = hours + 1;
			}
			min = 0;
			sec = 0;
		}
		
	}	
	pthread_mutex_unlock(&locked);
}

int main()  {
	pthread_t th1, th2, th3;
	
	
	time_t now;
	time(&now);

	
	struct tm *local = localtime(&now);
	hours = local->tm_hour;
	min = local->tm_min;
	sec = local->tm_sec;
	
	pthread_create(&th1, NULL, func1, NULL);
	pthread_create(&th2, NULL, func2, NULL);
	pthread_create(&th3, NULL, func3, NULL);

	while(1){
		
		printf("\r%02d : %02d : %02d", hours, min , sec);
		
	}
	
	pthread_join(th1, NULL);
	pthread_join(th2, NULL);
	pthread_join(th3, NULL);
	
	return 0;
}



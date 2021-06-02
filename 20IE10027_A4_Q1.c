//including header files
#include <stdio.h>
#include <math.h>

//start of main function
int main()
{
//initialising variables
//n--> stores the input
  int n;
  printf("Enter the size of the array:\n");
  scanf("%i",&n);

//using array of size n+2 so that we can use array indices till n+1
//arr[0] won't be used since integers entered in range 1 to n+1 
//arr[0](used as flag variable)--> stores 1 if an out-of-range value has been entered
  int arr[n+2];
  arr[n+1]=0;
//setting flag to 0(default state)  
  arr[0]=0;
  printf("Enter %i elements to store in array between 1 to %i in random order:\n",n,n+1);
  
//loop to intialise all array elements to zero
//also populates respective index if that number is present  
  for(int i=1;i<=n;i++)
  {
    int temp;
    arr[i]=0;
    scanf("%i",&temp);
    if(temp<n+2 && temp>0)
    {
      arr[temp]=1;
    }
    else
    {
    //flag set to 1 since out-of-range value encountered
      arr[0]=1;
    }
  }
  //we exit program if flag=1
  if(arr[0]==1)
  {
    printf("Error: Value-Out-of-Range");
    return 0;
  }
  //loop that detects missing value
  for(int i=1;i<=n+1;i++)
  {
    if(arr[i]!=1)
    {
      printf("The missing number is: %i",i);
      return 0;
    }
  }
  return 0;
}

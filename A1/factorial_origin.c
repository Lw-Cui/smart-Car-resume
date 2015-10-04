#define s8 char; 
int main()
{
    char answer;
    char a[5]={1;2;3;4;5};
    answer=calclate(1,&a,5);
    printf("%s",answer);
    return 0;
}
char calculate(s8 id,char *p,s8 n) //0<n<10
{
   s8 i;
   int ans;
   if(id=1)
   {
     ans=0;	
     for(i=0;i<=n;i++)
     	ans+=p[i]
	
   }
   else if(id=2)
   {
      ans=0;
      for(i=0;i<=n;i++)
     	ans+=p[i]
   }
   return ans; 
};

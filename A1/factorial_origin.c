// Warning: 'char' isn't a fit type for storing integer.
#define s8 char;  
int main()
{
    char answer;
    char a[5]={1;2;3;4;5}; // Error: initialize error.
    answer=calclate(1,&a,5);
    // Error: format error.
    printf("%s",answer);
    return 0;
}

// Error: return type doesn't match.
char calculate(s8 id,char *p,s8 n) //0<n<10
{
   s8 i;
   int ans;
   // Error: shouldn't use assignment.
   if(id=1)
   {
     ans=0;	
     // Error: overflow.
     for(i=0;i<=n;i++)
      // Error: syntax.
     	ans+=p[i]
	
   }
   else if(id=2)
   {
      ans=0;
      for(i=0;i<=n;i++)
        // Error: logical error.
     	ans+=p[i]
   }
   return ans; 
};

// https://www.codewars.com/kata/5545f109004975ea66000086/train/csharp

public class DivisibleNb 
{
  public static bool isDivisible(long n, long x, long y) 
  {
    if (n%x==0 && n%y==0) {
      return true;
    }
    else {
      return false;
    }
  }
}
package main

import "fmt"

func IsDivisible(n, x, y int) bool {
	return (n%x==0 && n%y==0)
}	


func main() {
	fmt.Println("Main")
	fmt.Println(IsDivisible(10,2,2))
}
package main

import (
    "bufio"
//    "strings"
    "fmt"
    "os"
)

func abs(a int, b int) int {
    if a - b < 0 {
        return (b - a)
    } else {
        return (a - b)
    }
}

func main() {

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
		s := scanner.Text()
        fmt.Printf("%v\n", s)
    }
}


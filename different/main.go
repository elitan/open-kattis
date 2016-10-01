package main

import (
    "bufio"
    "strings"
    "fmt"
    "os"
    "strconv"
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
        line_array := strings.Split(scanner.Text(), " ")
        a,_ := strconv.Atoi(line_array[0])
        b,_ := strconv.Atoi(line_array[1])
        fmt.Printf("%v\n", abs(a,b))
    }
}

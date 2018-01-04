package main

import "fmt"
import "time"

type Token struct {
  data string
  recipient int
  ttl int
}

//Функция, возвращающая поля Token
func (T *Token) get() (string, int, int) { return T.data, T.recipient, T.ttl }

func main() {
  //Ввод
  var N, r, t int
  var d string
  fmt.Printf("Enter N:")
  fmt.Scanf("%d", &N)
  fmt.Printf("Enter data:")
  fmt.Scanf("%s", &d)
  fmt.Printf("Enter recepient:")
  fmt.Scanf("%d", &r)
  for r > N {
    fmt.Printf("Error. Enter recepient again:")
    fmt.Scanf("%d", &r)
  }
  fmt.Printf("Enter ttl:")
  fmt.Scanf("%d", &t)
  
  T:= Token{data: d, recipient: r, ttl: t}
  
  //Основная часть
  Ch := make(chan Token)
  for i := 0; i < N; i++ {
    go Node(Ch, i)
  }
  
  Ch <- T
  //time.Sleep(1 * time.Second)
  fmt.Println(<-Ch)
}

func Node(Ch chan Token, n int) {
  T := <-Ch
  if T.ttl > 0 && T.recipient != n {
    T.ttl-=1
    time.Sleep(100 * time.Millisecond)
    Ch <- T
  } else{
    Ch <- T
  }
}
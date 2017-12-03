object Ex2 {
  def main(args: Array[String]) = {
    // Exercise 2.1
    println(fib(19))
    println(fib_b(19))

    // Exercise 2.2
    println(isSorted(Array(1, 2, 3, 4, 6) , (a: Int ,b: Int) => a < b ))
    println(isSorted(Array(2, 1, 3, 4, 6) , (a: Int ,b: Int) => a < b ))

    // Exercise 2.3
    val f = (x:Int, y:String) => x.toString + y 
    val hoge = curry(f)
    println(f)
    println(f(1, "hoge"))
    println(hoge(1)("hoge"))
  }

  def curry[A, B, C](f: (A, B) => C): A => B => C = 
    (a:A) => (b:B) => f(a, b)

  @annotation.tailrec
  def isSorted[A](as: Array[A], ordered: (A, A) => Boolean): Boolean = {
    val head = as.head
    val rest = as.tail
    if (rest.isEmpty) 
      true
    else if (ordered(head, rest.head))
      isSorted(rest, ordered)
    else
      false
  }
  

  def fib(tn: Int): Int = {
    @annotation.tailrec
    def fib_n(n_2: Int, n_1:Int, n: Int):Int = {
      if (n == tn) {
        n_2 + n_1
      } else {
        fib_n(n_1, n_2+n_1, n+1)
      }
    }
    if (tn == 0)
      0
    else if (tn == 1) 
      1
    else
      fib_n(0,1,2)
  }
  
  def fib_b(n: Int): Int = {
    if (n <= 0) {
      0
    } else if (n == 1) {
      1
    } else {
      fib(n-2) + fib(n-1)
    }
  }

}


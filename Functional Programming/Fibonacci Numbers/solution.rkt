(define fibonacci
  (lambda (n)
    (let fib ([i n])
      (cond
        [(= i 0) 0]
        [(= i 1) 1]
        [(or (= i 2) (= i 3)) 1]
        [else (+ (fib (- i 1)) (fib (- i 2)))]))))
        
(fibonacci (read))
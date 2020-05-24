;;;Factorial without recursion
(princ "Factorial without recursion\n ")
(terpri)
(princ "Enter a number: ")
(setq p (read))

(defun fact (n)
   (let ((f 1))
      (dotimes (i n) 
         (setf f (* f (+ i 1))))
      f
   )
)

(setq fact (fact p))
(princ "Factorial: ")
(write fact)
(terpri)

;;;Factorial With Recursion
(princ "Factorial with recursion ")
(terpri)
(princ "Enter a number: ")
(setq p (read))

(defun factorial (n)
  (if (= n 0)
      1
      (* n (factorial (- n 1))) ) )

(setq fact (factorial p))
(princ "Factorial: ")
(write fact)
(terpri)


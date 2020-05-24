;;;Finding nth element of list


(defun nlist(n lst)
       (let((count 1))
           (loop
               (cond((equal count n)(return (car lst))))
               (setq count (+ count 1))
               (setq lst (cdr lst)))))    






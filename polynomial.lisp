(defun poly-substitute (n poly value)
  (if (or (> n (poly-order poly)) (< n 0))
      poly
      (if (> n 0)
	  (cons (car poly) (poly-substitute (- n 1) (cdr poly) value))
	  (cons value (cdr poly)))))

(defun poly-make (&rest values)
  values)

(defun poly-order (poly)
  (- (length poly) 1))

(defun poly-nth (n poly)
  (let ((index-value (nth n poly)))
    (if (not index-value) (setf index-value 0))
    index-value))
    
(defun poly-max-order (&rest poly-set)
  (let ((max-order 0))
    (dolist (poly poly-set max-order)
      (let ((order (poly-order poly)))
	(if (> order max-order)
	  (setf max-order order))))))

; Use the friendlier polynomial output function poly-print.
; This is for debugging only
(defun newline () (format t "~%"))
(defun print-list (nlist)
  (format t "~{~D~^, ~}" nlist))

(defun poly-print (poly)
  (let ((nlist (reverse poly)) (print-index (poly-order poly)))
    (dolist (index-value nlist NIL)
      (progn
	(if (not (= print-index 0)) (format t "~fx^~d + " index-value print-index) (format t "~f" index-value))
	(setf print-index (- print-index 1))))))


(defun poly-add (&rest poly-set)
  (let ((max-order (apply #'poly-max-order poly-set)) (poly-add-result NIL)) 
    (dotimes (index max-order poly-add-result)
      (setf poly-add-result (cons 
			     (let ((index-sum 0))
			       (dolist (poly poly-set index-sum)
				 (setf index-sum (+ index-sum (poly-nth index poly))))) 
			     poly-add-result)))
    (reverse poly-add-result)))

; Test this function
(defun poly-mult-two (poly-a poly-b)
  (if (and poly-a poly-b)
      (let ((poly-result '()))
	(dotimes (index-a (+ 1 (poly-order poly-a)) poly-result)
	  (dotimes (index-b (+ 1 (poly-order poly-b)) poly-result)
	    (let ((loc (+ index-a index-b)))
	      (if (> loc (poly-order poly-result))
		  (setf poly-result 
			(reverse (cons (* (poly-nth index-a poly-a) (poly-nth index-b poly-b)) (reverse poly-result))))
		  (setf poly-result (poly-substitute loc 
						     poly-result
						     (+ (* (poly-nth index-a poly-a) (poly-nth index-b poly-b))
							(poly-nth loc poly-result)))))))))
      NIL))
						 

(defun poly-mult (&rest poly-set)
   (if (> (length poly-set) 0)
      (if (car poly-set)
	  (poly-mult-two (car poly-set) (apply #'poly-mult (cdr poly-set)))
	  NIL)
      (poly-make 1)))
 

 
      
; Test data	    
(defvar a (poly-make 2 3 4 7))
(defvar b (poly-make 2 3 4 7 5))
(defvar c (poly-add a b))
(poly-print a)
(newline)
(poly-print b)
(newline)
(poly-print c)
(newline)
(poly-print (poly-substitute 0 c 5))


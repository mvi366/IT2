

## oppgave 1
C
## oppgave 2
C
## oppgave 3
C 
## oppgave 4
C
## oppgave 5
D
## oppgave 6
nr 1 og 4
## oppgave 7
bilde i mappe

## oppgave 8

FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION

FUNCTION beregn_totalsum()
  SET totalsum TO 0
  FOR i FROM 1 TO 10
    SET trekanttall_i TO trekanttall(i)
    SET totalsum TO totalsum + trekanttall_i
  ENDFOR
  RETURN totalsum
ENDFUNCTION




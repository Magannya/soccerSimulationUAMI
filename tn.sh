!#/bin/bash

for i in {1..5}; do
	python3 t1.py &
done

for i in {1..5}; do
	python3 t2.py &
done

wait

echo "(y)"

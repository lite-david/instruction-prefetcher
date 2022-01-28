if [ "$#" -ge 1 ]; then
  PATTERN="*$1*"
else
  PATTERN="*"
fi
grep "L1I LOAD" ./$PATTERN | awk '{print $1",", $4",",$8}' > $1_l1i.csv
grep "^CPU 0 cumulative IPC" ./$PATTERN | awk '{print $1",", $5}' > $1_ipc.csv

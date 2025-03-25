COMMIT=$(git log --no-merges -n 100 --pretty=format:"%H")

mkdir -p Results

counter=1
for i in $COMMIT; do
  git checkout $i
  bandit -r . -f json -o Results/$counter.json
  counter=$((counter + 1))
done

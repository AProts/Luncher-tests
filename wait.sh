while ! nc -z luncher 3000; do
echo WAITING...;
sleep 5;
done

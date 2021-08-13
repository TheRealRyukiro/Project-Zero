clear
echo "Refreshing Github Repository Script by Tommy :)"
echo "You are free to minimize this window. Your files will sync every 3 seconds."
sleep 5
while :
do
	echo "Sending a request to pull for updated files..."
	git pull
	echo "Sending a request to push updated files..."
	git push
	sleep 3
	clear
done

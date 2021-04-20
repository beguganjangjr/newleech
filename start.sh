file="trackers.txt"
echo "$(curl -Ns https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt)" > trackers.txt
echo "$(curl -Ns https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt)" >> trackers.txt
tmp=$(sort trackers.txt | uniq) && echo "$tmp" > trackers.txt
sed -i '/^$/d' trackers.txt
sed -i ":a;N;s/\n/,/g;ta" trackers.txt
tracker_list=$(cat trackers.txt)
if [ -f $file ] ; then
    rm $file
echo "trackers added"
fi
echo "bt-tracker=$tracker_list" >> aria2c.conf

if [[ -n $RCLONE_CONFIG ]]; then
 echo "Rclone config detected"
 echo -e "$RCLONE_CONFIG" > /app/rclone.conf
fi
python3 -m tobrot

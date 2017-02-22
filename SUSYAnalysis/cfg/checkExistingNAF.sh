echo $1
move=0
if [ $1 == "move" ]
then
	move=1
fi
echo $move

if [ $move == 1 ]; then echo "will move files"; else echo "will just list"; fi
for dir in */
do
    #echo $dir
	if [ ! -f $dir/skimAnalyzerCount/SkimReport.txt ]
	then
#		echo $dir/skimAnalyzerCount/SkimReport.txt
		echo $dir
		cd $dir
#		ls
		if [ $move == 1 ]; then rm processed && rm -R -- */ ; fi
#		rm -R -- */
		cd ..
		if [ $move == 1 ]; then mv $dir ../. ; fi
	fi
done


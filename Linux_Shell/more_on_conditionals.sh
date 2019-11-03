read X
read Y
read Z

if [[ ($X != $Y && $Y != $Z) && $X != $Z ]];
then echo SCALENE
elif [[ $X == $Y && $Y == $Z ]];
then echo EQUILATERAL
else echo ISOSCELES
fi


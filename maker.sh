#! /bin/bash

if [ $# -eq 1 ]; then
    if [ $1 = "png" ]; then
        echo -n "title : "
        read title
        #ls -t1 /Pictures/ | tail -2 | xargs -I {} mv {} flashcards/$title/
        mkdir flashcards/$title/
        ls -t1 ~/Pictures/ | head -2 | xargs -I {} mv ~/Pictures/{} flashcards/$title/

        firstOne=true
        for file in flashcards/$title/*; do
            if $firstOne; then
                mv $file "flashcards/$title/${title}Q.png"
                firstOne=false
            else 
                mv $file "flashcards/$title/${title}A.png"
            fi
        done

    elif [ $1 = "txt" ]; then
        echo -n "title : "
        read title
        codium "flashcards/$title/${title}A.txt"
        codium "flashcards/$title/${title}Q.txt"
    else
        echo put txt or png as argument
        exit
    fi
else 
    echo put txt or png as argument
    exit
fi
exit
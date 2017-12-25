First mapreduce computes mean values of *prodTime* for every *antiNucleus*
Second mapreduce filters only these entries which contain *prodTime* > mean value per *antiNucleus*. Then calculates the number of unique *eventFile* and mean value of *Pt*

To run it first make sure all the files from this repository (except results.txt) as well as data file are in the right place. One can load these files like follows:

  1. Create <name>.sh file:

    docker exec $1 mkdir -p scripts
    for f in mapper1.py mapper2.py reducer1.py reducer2.py star2002-sample.csv command.sh; do
        docker cp $f $1:/scripts/$f
    done
    
  2. Add permissions and run this file
  
    sudo chmod +x <name>.sh
    sudo ./<name>.sh <docker_id>

Then simply run **command.sh** script from the *script/* folder in docker. It'll produce result file named *results.txt*

#! /bin/zsh

help() {
    echo """
    sp
    
    Competitive Programming related functinality

    commands:
    -------------
    <file_name>                                         Create file with $HOME/.sp/template.cpp
    update <template_name>                              update template in $HOME/.sp/template.cpp
    run <file_name>                                     Run C/C++ code with runtime info
    compile <file_name>                                 Compile C/C++ with log details
    cfstatus  <numaric seriels> <alfabic seriels>       Problem submission status
    help                      For help
    """
}

if [[ $1 == --help || $1 = "" ]]
then
    help
elif [[ $1 == run ]]
then
    g++ $2 && time ./a.out
elif [[ $1 == compile ]]
then
    g++ -v $2
elif [[ $1 == update ]]
then
    cp -v $2 $HOME/.sp/template.cpp
elif [[ $1 == ac ]]
then
    current_date=$(date '+%r (%Z)')
    echo "// Accepted: $current_date" >> $2
elif [[ $1 == cfstatus ]]
then
    google-chrome "https://codeforces.com/problemset/status/$2/problem/$3?friends=on"
else
    file_name=$1
    file_name=${file_name// /_}
    file_name=${file_name//._/.}
    if [[ $2 != "" ]]
    then
        file_name="$file_name.$2"
    fi
    
    echo "Creating the $file_name file... Done."
    cp ~/.sp/template.cpp $file_name
    current_date=$(date '+%A, %B %d, %Y | %r (%Z)')
    echo "// $current_date" >> $file_name
    # echo "// Problem Link: $2" >> $1
    echo "Done! let's play"
    code $file_name
fi

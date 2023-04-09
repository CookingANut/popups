#!/usr/bin/bash

function add_alias 
{
    printf "alias $ADD_ALIAS" >> ~/.bashrc
}

function remove_alias 
{
    REMOVE_ALIAS="$(sed -e 's/[\/&]/\\&/g' <<< $REMOVE_ALIAS)"
    sed -i "s/alias $REMOVE_ALIAS/d" ~/.bashrc

}

function help
{
    echo "-a/--add={the alias expression you want to add}"
    echo "-r/--remove={the alias expression you want to remove}"
    exit 0
}


for i in "$@"; do
  case $i in
    -a=*|--add=*)
      ADD_ALIAS="${i#*=}"
      add_alias
      shift # past argument=value
      ;;
    -r=*|--remove=*)
      REMOVE_ALIAS="${i#*=}"
      remove_alias
      shift # past argument=value
      ;;
    -h|--help)
      help
      shift # past argument=value
      ;;
    -*|--*)
      echo "unknown argument $i"
      exit 1
      ;;
    *)
      ;;
  esac
done

if [ -n $ADD_ALIAS ]; then
    echo "ADD_ALIAS    = ${ADD_ALIAS}"
fi

if [ -n $REMOVE_ALIAS ]; then

    echo "REMOVE_ALIAS = ${REMOVE_ALIAS}"
fi



#!/bin/bash


while true
do
	canasta_pid=$(pgrep python)
	top -p $canasta_pid
	sleep 10
done

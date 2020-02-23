#!/usr/bin/awk -f

BEGIN { 

        FIELDS_LIST = ARGV[1]
	split(FIELDS_LIST,fields_array,",")
	delete ARGV[1]
}

{FS = "," }

{ for (i in ARGV)
	for (j in fields_array)
		{ print $fields_array[j] } ARGV[i]
}

END {
	printf "end"
}

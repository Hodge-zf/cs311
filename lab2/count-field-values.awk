#!/usr/bin/awk -f

BEGIN { 

        FIELDS_LIST = ARGV[1]
	split(FIELDS_LIST,fields_array,",")
	delete ARGV[1]
}

{ FS = "," }

{
	for (j in fields_array)
			if (FNR > 1)
				{ value_count[$fields_array[j]]++ }
	
}

END { 
	for(i in value_count) 
		print value_count[i],i
	
}

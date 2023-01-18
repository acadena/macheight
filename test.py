values = input("Please input values: ").split( " " )
array = values[0].split( "," )
sum = int(values[1])

index = 1
success = []
array_len = len(array)
for value in array:
    i = index
    while i < array_len:
        if( int(value) + int(array[i]) == sum ):
            success.append( value + " " + array[i] ) 
        i += 1
    index += 1

print( success )

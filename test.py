import math

values = input("Please input values: ").split( " " )
array = values[0].split( "," )
sum = int(values[1])

success = []
exist = []
array_len = len(array)-1
mid_array = math.floor(array_len/2)

for value in array:
   
    i = 1
    k = array_len

    while i <= (mid_array) and k >= 0:

        if( int(value) + int(array[i]) == sum and
            not array[i] in exist and
            int(value) != int(array[i])
        ):
            success.append( value + " " + array[i] )
            exist.append(value)

        if( int(value) + int(array[k]) == sum and
            not array[k] in exist and
            int(value) != int(array[k])
        ):
            success.append( value + " " + array[k] )
            exist.append(value)

        i += 1
        k -= 1

print( success )

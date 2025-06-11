input_file=input("Enter the source file name:")
output_file=input("Enter the destination file name:")
try:
    with open(input_file,'r')as infile: #reasing from a file
        read=infile.read()
    with open(output_file,'w') as outfile:   #writing from a file
        outfile.write(read)
    with open(output_file,'r')as output:     # checking the output file
        content=output.read()
        print(content)
except FileNotFoundError:
    print(f" Error: {input_file} was not found!")  # error checking
except Exception as e:
    print(e)





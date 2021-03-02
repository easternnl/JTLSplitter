import argparse
import os

# parse the arguments
parser = argparse.ArgumentParser()

parser.add_argument('--input', help='JTL logfile to process', required=True)
parser.add_argument('--output', help='JTL logfile to write to', required=True)
parser.add_argument('--split', type=int, default=1000000, help='How much lines before splitting')
parser.add_argument('--verbose', default=0, help='Display all parameters used in the script')


args = parser.parse_args()

# Show arguments if verbose
if (args.verbose):    
    print("input=%s" %(args.input))
    print("output=%s" %(args.output))



print("Splitting: %s" % (args.input))

output_filename, output_extension = os.path.splitext(args.output)
header = None
filecounter = 0

with open(args.input) as fp:  
    # first save the header
    header = next(fp)

    for cnt, line in enumerate(fp):
        if cnt % args.split == 0:
            # create a new file
            filecounter = filecounter + 1
            
            try:
                output.close()
            except:
                pass

            print("Output to %s%d%s  made %d" % (args.output, filecounter, output_extension, cnt))
            output = open("%s%d%s" % (output_filename, filecounter, output_extension), "w+")
            output.write(header)

        output.write(line)

    output.close()

            



    
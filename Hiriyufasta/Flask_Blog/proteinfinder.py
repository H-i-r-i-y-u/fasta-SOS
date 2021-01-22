import re


def proteinfind(sequence,filename,name):
    sequence = str(sequence)

    with open(filename) as f_input, open('output'+name+'.fasta', 'w') as f_output:

        block = []
        previousline = " "
        for line in f_input:
            if line.startswith('>'):
                if block:
                    m = re.search(sequence, block[0])
                    if m:
                        f_output.write("consensus sequense found!")
                        f_output.write("at position " + str(m.start()))
                        f_output.write(m.group())
                        f_output.write(previousline)

                    block = []
                previousline = line

            else:
                block.append(line.strip())

        if block:

            m = re.search(sequence, block[0])
            if m:
                f_output.write("consensus sequense found!")
                f_output.write("at position " + str(m.start()))
                f_output.write(line)


pass

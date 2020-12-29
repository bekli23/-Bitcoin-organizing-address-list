#Run with python 2.7  and 3.9
##############################################################
################Acest program este facut de catre bekli23 ####
################Nu copii-a ###################################
def main():
    with open("list-All.txt") as infile, open("output.txt", "w") as outfile:
        lines = [line.strip(" ") for line in infile if line != "\n"]
        lines.sort()
        for line in lines:
            outfile.write(line)

if __name__ == '__main__':
    main()
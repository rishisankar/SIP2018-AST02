import os

if __name__ == '__main__':
    tf1 = open("RMFtags.txt", "r")
    tf2 = open("Disktags.txt", "r")
    tags = []
    for line in tf1.readlines():
        try:
            tags.append(int(line[:-1]))
        except Exception:
            continue
    for line in tf2.readlines():
        try:
            tags.append(int(line[:-1]))
        except Exception:
            continue
    f = open("generated_runscript.sh","w")
    for filename in os.listdir("."):
        if filename.endswith("_sig.fits"):
            continue
        if filename.endswith(".fits"):
            run = True
            for tag in tags:
                if str(tag) in filename:
                    run = False
                    break
            if run:
                file = filename[:-5]
                f.write("./isofit_model.sh " + file + " remove\n")
    f.write("\n")
    f.close()

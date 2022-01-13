import subprocess


def file_to_pdf(inputFileName, outputFileName):
    # convert(inputFileName, outputFileName)
    print("Before Docs to PDF")
    cmd = (
            "libreoffice --headless --invisible --convert-to pdf "
            + inputFileName
            + " --outdir /home/pc/Downloads/save.pdf"
    )
    subprocess.run(cmd.split())
    print("Converted Docs to PDF")

file_to_pdf('/home/pc/Downloads/file_example_PPT_250kB.pdf','save.pdf')

# libreoffice --headless --invisible --convert-to pdf /home/pc/Downloads/file-sample_100kB.doc --outdir /home/pc/Downloads/save.pdf
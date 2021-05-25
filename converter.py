import imageio
import os

class Gifeo:
    def __init__(self,urlPath):
        self.url = urlPath

    def converter(self,targetFormat):
        outputPath = os.path.splitext(self.url)[0] + targetFormat
        print(f'converting {self.url} \n to {outputPath}')
        reader = imageio.get_reader(self.url)
        fps = reader.get_meta_data()['fps']
        writer = imageio.get_writer(outputPath,fps=fps)
        for frame in reader:
            writer.append_data(frame)

        print('Successfully converted')
        writer.close()




gif1 = Gifeo(input("Please enter the path of the video to convert into a gif: "))
gif1.converter(".gif")





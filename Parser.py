## This class will parse VCF file into data structure as needed

class VCF_Parser:

    def __init__(self, vcf_path):
        self.file_path = vcf_path
        self.vcf_dict = self.parse()

    def parse(self):
        dict = {}
        with open(self.file_path, 'r') as f:
            lines = [l for l in f if not l.startswith('##')]

        for idx, l in enumerate(lines):
            if idx == 0:
                for key in lines[0].split("\t"):
                dict[key] = []

            else:





        return dict




if __name__ == '__main__':
    p = VCF_Parser("data/sample.vcf")
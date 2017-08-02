import vcf
def vcf_2_bed(input_vcf,vcf_bed):
    """
    For some reason, some samples don't have any bed file to use.
    Like some WGS or untold sample, we need to self-cal the bed file from the vcf incase to reduce the low coverage point.

    Vcf is 1-based coordinate and left close,right close intervals.
    bed is 0-based coordiante and left close,right open intervals.
    :param input_vcf:
    :param vcf_bed:
    :return:
    """
    vcf_record = vcf.Reader(filename=input_vcf)
    bed_str = ''
    for _record in vcf_record:
        chr = _record.CHROM
        POS = int(_record.POS)
        REF = _record.REF
        ALT = _record.ALT
        max_ALT_length = max([len(_alt) for _alt in ALT])

        bed_str += chr+'\t'+ str(POS-1) +'\t' + str(POS-1+max(max_ALT_length,len(REF))) +'\n'

    with open(vcf_bed,'w') as f1:
        f1.write(bed_str)



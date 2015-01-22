###Practice program. Changes a DNA sequence to an RNA sequence.
###followed by the complement. Converts codons to AA.

#Sequence of interest
Seq="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"

#Finding and printing the length of the sequence

length=(len(Seq))
print("The length of the DNA sequence is: ", length, "bases.")

#Converting the DNA sequence to its RNA equivalent

RNA=Seq.replace("t","u")

print("The RNA sequence is: ", RNA)


#Finding the reverse complement of the DNA sequence

#Attempting to reverse the sequence...

revSeq=Seq[::-1]

#Replacing nucleotides for complement

revComp=revSeq.replace("a","T").replace("t","a").replace("T", "t").replace("c","G").replace("g","c").replace("G","g")

#printing reverse complement

print("The reverse complement of the sequence is: ",revComp)

#Removed the last two bases from the initial sequence and stored again

dnaSeq="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggc"

#printing the 13th and 14th codon from the sequence

cthirteen=dnaSeq[36:39]

cfourteen=dnaSeq[39:42]

print ("The 13th codon in the sequence is: ", cthirteen)

print("\n")

print("The 14th codon in the sequence is: ", cfourteen)

##splitting the codons

#empty list for codons
z=[]

#using a for loop to loop through all of nt 3 at a time
for codon in range(0,len(dnaSeq),3):
    #appending them to list z, capitalizing the nts.
    z.append(dnaSeq.upper()[codon:codon+3])


#Creating a dictionary for the mitochondrial amino acids/codons

AAs= {'TTT': 'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
      'TCT':'S', 'TCC':'S', 'TCA': 'S', 'TCG':'S',
      'TAT':'Y', 'TAC':'Y', 'TAA': '*', 'TAG':'*',
      'TGT':'C', 'TGC':'C', 'TGA':'W', 'TGG':'W',
      'CTT':'L', 'CTC': 'L', 'CTA': 'L', 'CTG':'L',
      'CCT':'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
      'CAT':'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
      'CGT': 'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
      'ATT': 'I', 'ATC':'I', 'ATA':'M', 'ATG':'M',
      'ACT':'T', 'ACC':'T', 'ACA': 'T', 'ACG':'T',
      'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG': 'K',
      'AGT':'S', 'AGC': 'S', 'AGA': '*', 'AGG': '*',
      'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
      'GCT': 'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
      'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
      'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

#Creating a blank list for proteins

y=[]

#Looping through all the codons in the list of codons, z
for codons in z:
#appending the empty list above with the appropriate protein for that amino acid
    y.append(AAs.get(codons))

##printing the list of proteins

#Removing brackets and commas from the list of amino acids
aalist=''.join(y)

#printing out the aminoacids
print("The amino acids sequence generated from this DNA sequence is: ", aalist)
